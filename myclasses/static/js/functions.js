const syllabusButton = document.getElementById('syllabus_button');
    const fileChosen = document.getElementById('file_chosen');
    syllabusButton.addEventListener('change', function() {
        fileChosen.textContent = this.files[0].name;
    });

function openNav() {
    document.getElementById("collapsableSidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
};
function closeNav() {
    document.getElementById("collapsableSidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
};