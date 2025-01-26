
from django.shortcuts import render

# Create your views here.

from pydoc import classname
import google.generativeai as genai
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Note, Syllabus
from django.conf import settings

genai.configure(api_key = "AIzaSyCxaAG8-_RT0HTdJKMvslNH7hLdSpDMuM8")



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
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content("Summarize the given notes in an informative way so as to maximize the user's understanding")

                summary = response.text
                note.summary = summary
                note.save()
            except RuntimeError as e:
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
