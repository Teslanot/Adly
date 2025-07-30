const toggleBtn = document.getElementById('toggle-posts');
const postsList = document.getElementById('posts-list');

toggleBtn.addEventListener('click', () => {
    const isHidden = postsList.classList.toggle('hidden');
    toggleBtn.textContent = isHidden ? 'Показать мои объявления' : 'Скрыть мои объявления';
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

document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-adv');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            const advId = button.dataset.id;

            if (!confirm('Вы уверены, что хотите удалить это объявление?')) return;

            try {
                const response = await fetch(`/profile/adv/delete/${advId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });

                const data = await response.json();
                if (data.success) {
                    document.getElementById(`adv-${advId}`).remove();
                } else {
                    alert(data.message || 'Ошибка удаления');
                }
            } catch (err) {
                console.error(err);
                alert('Ошибка при отправке запроса');
            }
        });
    });
});