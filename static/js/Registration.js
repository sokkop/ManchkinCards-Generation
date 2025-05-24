document.getElementById('RegisterForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
        login: document.getElementById("login").value,
        password: document.getElementById("password").value
    };

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Ошибка регистрации');
        }

        const result = await response.json();
        alert('Регистрация успешна!');
        window.location.href = '/'; // Перенаправление на страницу входа
    } catch (error) {
        console.error('Error:', error);
        alert('Ошибка: ' + error.message);
    }
});