document.addEventListener('DOMContentLoaded', function() {
  const faqToggles = document.querySelectorAll('.faq-toggle');

  faqToggles.forEach(function(toggle) {
    toggle.addEventListener('change', function() {
      const answer = this.parentNode.querySelector('.faq-answer');
      const icon = this.parentNode.querySelector('.faq-icon i');

      answer.style.display = this.checked ? 'block' : 'none';
      icon.className = this.checked ? 'fas fa-minus' : 'fas fa-plus';
    });
  });
});
