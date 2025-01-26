from pydoc import classname
import openai
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Note, Syllabus
from django.conf import settings

openai.api_key = ""

def notes_view(request, title, syllabus_id):
    user = request.user
    selected_class = get_object_or_404(Syllabus, id=syllabus_id, title=title)
    notes = Note.objects.filter(user=user,className=selected_class)


    if request.method == "POST":
        uploaded_file = request.FILES.get("note_file")
        pasted_text = request.POST.get("note_text")

        if uploaded_file or pasted_text:
            content = ""
            head = ""
            summary = ""

            if uploaded_file:
                content = uploaded_file.read().decode("utf-8")
                head = "File Note"
            else:
                # Use pasted text if no file is uploaded
                content = pasted_text
                head = "Pasted Note"

            note = Note.objects.create(
                user=user,
                title=head,
                content=content,
                className = selected_class
            )

            try:
                ###
                response = openai.completions.create(
                model="gpt-3.5-turbo",
                prompt=f"Summarize the following text:\n{content}",
                temperature=0.5,
                max_tokens=100,  # Adjust as needed
            )
                summary = response["choices"][0]["text"].strip()
                note.summary = summary
                note.save()
            except openai.OpenAIError as e:
                note.summary = f"Error summarizing note: {str(e)}"
                note.save()
            ####

    # Check if there are any notes and pass a flag
    notes_exist = notes.exists()

    for note in notes:
        print(f"Note title: {note.title}, Summary: {note.summary}")

    return render(request, "study/notes.html", {
        "title":title,
        "syllabus_id":syllabus_id,
        "notes": notes,
        "notes_exist": notes_exist,
        "selected_class": selected_class,
    })
