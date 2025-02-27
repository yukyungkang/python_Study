document.addEventListener("DOMContentLoaded", function () {
    fetch("nav.html")
        .then(response => response.text())
        .then(data => {
            document.body.insertAdjacentHTML("afterbegin", data);
        })
        .catch(error => console.error("네비게이션을 불러오는 데 실패했습니다.", error));
});

// 반응형 메뉴 토글 기능
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}
