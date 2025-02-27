document.addEventListener("DOMContentLoaded", function () {
    fetch("nav.html")
        .then(response => {
            if (!response.ok) {
                throw new Error("네비게이션 파일을 찾을 수 없습니다.");
            }
            return response.text();
        })
        .then(data => {
            document.body.insertAdjacentHTML("afterbegin", data);
            applyStyles(); // 네비게이션이 로드된 후 스타일 적용
        })
        .catch(error => console.error("네비게이션 로드 중 오류 발생:", error));
});

function applyStyles() {
    const styleSheet = document.createElement("link");
    styleSheet.rel = "stylesheet";
    styleSheet.href = "styles.css"; // 스타일 적용
    document.head.appendChild(styleSheet);
}

// 메뉴 토글 기능
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}
