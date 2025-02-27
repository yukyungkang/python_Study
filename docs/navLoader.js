document.addEventListener("DOMContentLoaded", function () {
    fetch("nav.html")  // nav.html을 불러오기
        .then(response => {
            if (!response.ok) {
                throw new Error("네비게이션 파일을 찾을 수 없습니다.");
            }
            return response.text();
        })
        .then(data => {
            document.body.insertAdjacentHTML("afterbegin", data); // <body> 내부 가장 위에 삽입
            addMenuToggle(); // 네비게이션이 로드된 후 메뉴 토글 기능 추가
        })
        .catch(error => console.error("네비게이션을 불러오는 중 오류 발생:", error));
});

function addMenuToggle() {
    const menuToggle = document.querySelector('.menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function () {
            const menu = document.querySelector('.menu');
            if (menu) {
                menu.classList.toggle('active');
            }
        });
    }
}
