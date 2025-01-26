function openNav() {
    document.getElementById("collapsableSidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
};
function closeNav() {
    document.getElementById("collapsableSidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
};

document.getElementById('syllabus').addEventListener('change', function() {
    let fileName = this.files[0].name ? this.files[0].name : 'No file chosen';
    document.getElementById('fileName').textContent = 'Selected file' + fileName;
});