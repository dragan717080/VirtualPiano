const musicSheetContent = document.getElementById('sheet__content_value');

const editMusicSheet = (sheet) => {
    musicSheet = musicSheet.substr(2, musicSheet.length - 3);
    return musicSheet.replace(/\\r\\n/g, '<br>');
}

musicSheetContent.innerHTML = editMusicSheet(musicSheet);
