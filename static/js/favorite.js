document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('page-enter');
    setTimeout(() => {
        document.body.classList.add('page-enter-active');
    }, 100);

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();

        if (cookie.startsWith(name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
        }
    }
    return cookieValue;
}

document.addEventListener('click', function (e) {
    if (e.target.classList.contains('fav_toggle')) {
        const button = e.target;
        const advId = button.dataset.advId;
        const action = button.dataset.action;
        const url = action === 'add'
        ? `/add_to_favorites/${advId}/`
        : `/remove_from_favorite/${advId}/`;

        fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json'
        }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
            if (action === 'add') {
                button.textContent = 'Удалить из избранного';
                button.dataset.action = 'remove';
                button.classList.remove('from-blue-500', 'to-blue-600');
                button.classList.add('from-red-500', 'to-red-600');
            } else {
                button.textContent = 'Добавить в избранное';
                button.dataset.action = 'add';
                button.classList.remove('from-red-500', 'to-red-600');
                button.classList.add('from-blue-500', 'to-blue-600');
            }
            }
        })
        .catch(error => console.error(error));
    }
});

window.addEventListener("pageshow", function (event) {
    if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
        window.location.reload();
    }
});