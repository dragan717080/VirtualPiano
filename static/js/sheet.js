const musicSheetContent = document.getElementsByClassName("music-sheet__sheet-content_content")[0];

function editMusicSheet(sheet) {
    musicSheet = musicSheet.substr(2, musicSheet.length - 3);
    musicSheet = musicSheet.replace(/\\r\\n/g, "<br>");
    return musicSheet;
}

musicSheetContent.innerHTML = editMusicSheet(musicSheet);