document.getElementById('getDataBtn').addEventListener('click', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').textContent = JSON.stringify(data);
        });
});

document.getElementById('postDataBtn').addEventListener('click', () => {
    fetch('/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ key: 'new value' })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').textContent = JSON.stringify(data);
        });
});
