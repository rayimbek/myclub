
document.addEventListener('DOMContentLoaded', function() {

  const faqToggles = document.querySelectorAll('.faq-toggle');

  faqToggles.forEach(function(toggle) {
    
    toggle.addEventListener('change', function() {
      
      const answer = this.parentNode.querySelector('.faq-answer');

      const question = this.parentNode.querySelector('.faq-question');
      const icon = this.parentNode.querySelector('.faq-icon i');

      answer.style.display = this.checked ? 'block' : 'none';

      if(answer.style.display == 'block'){
         question.style.backgroundColor = '#05043A'
        question.style.color = 'white'
      }else{  
         question.style.backgroundColor = '#f2f2f2'
        question.style.color = '#05043A'
      }
      icon.className = this.checked ? 'fas fa-minus' : 'fas fa-plus';
    });
  });
});
