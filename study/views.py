import openai
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Note
from django.conf import settings

openai.api_key = "api key"

def notes_view(request):
    user = request.user
    notes = Note.objects.filter(user=user)


    if request.method == "POST":
        uploaded_file = request.FILES.get("note_file")
        pasted_text = request.POST.get("note_text")

        if uploaded_file or pasted_text:
            content = ""

            if uploaded_file:
                content = uploaded_file.read().decode("utf-8")
                title = "File Note"
            else:
                # Use pasted text if no file is uploaded
                content = pasted_text
                title = "Pasted Note"

            note = Note.objects.create(
                user=user,
                title=title,
                content=content,
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Summarize the text below."},
                        {"role": "user", "content": content},
                    ],
                    temperature=0.5,
                )
                note.summary = response["choices"][0]["message"]["content"]
                note.save()
            except openai.error.OpenAIError as e:
                note.summary = f"Error summarizing note: {str(e)}"
                note.save()

        # Redirect to the same page after handling the request
        return redirect("notes")

    # Check if there are any notes and pass a flag
    notes_exist = notes.exists()

    return render(request, "notes.html", {
        "notes": notes,
        "notes_exist": notes_exist
    })

def upload_note_view(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("note_file")
        if uploaded_file:
            # Read file content
            file_content = uploaded_file.read().decode("utf-8")

            # Save note
            Note.objects.create(
                user=request.user,  # Assuming notes are tied to the logged-in user
                title=os.path.basename(uploaded_file.name),  # Use the filename as the title
                content=file_content,
            )

        return redirect("notes_page")  # Redirect back to the notes page
    return redirect("notes_page")

def summarize_note_view(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        pass

    
    summary = None

    if request.method == "POST":
        try:
            # OpenAI API call for summarization
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Summarize the text below."},
                    {"role": "user", "content": note.content},
                ],
                temperature=0.5,
            )
            summary = response["choices"][0]["message"]["content"]

            # Save the summary if needed
            note.summary = summary
            note.save()

        except openai.error.OpenAIError as e:
            summary = f"Error: {str(e)}"

    return render(request, "notes.html", {"note": note, "summary": summary})
