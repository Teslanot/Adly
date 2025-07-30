document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.fade-in');
    if (form) {
        setTimeout(() => {
        form.style.opacity = '1';
        form.style.transform = 'translateY(0)';
        }, 200);
    }
});