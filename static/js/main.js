const closeBtn = document.querySelector('.close-btn');
const alert = document.querySelector('.alert');

closeBtn.addEventListener('click', () => {
  alert.style.display = 'none';
});
