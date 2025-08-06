fetch('/api/menu')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById('menu-list');
    data.forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `<strong>${item.name}</strong> - ${item.description} <span class="price">₹${item.price}</span>`;
      list.appendChild(li);
    });
  })
  .catch(err => {
    console.error('Failed to load menu', err);
  });
