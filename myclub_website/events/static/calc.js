function calculateGPA() {
  const course1 = Number(document.getElementById('course1').value);
  const course2 = Number(document.getElementById('course2').value);
  // Add more variables for additional courses

  const totalCredits = 8; // Update with the total number of credits
  const totalGPA = (course1 + course2) / totalCredits * 100; // Update the calculation for more courses

  const progressFill = document.querySelector('.progress-fill');
  const progressText = document.querySelector('.progress-text');
  
  progressFill.style.clip = `rect(0, ${totalGPA}px, 120px, 0)`;
  progressText.textContent = `${totalGPA.toFixed(1)}%`;
}

const inputs = document.querySelectorAll('input[type="number"]');
inputs.forEach(input => input.addEventListener('input', calculateGPA));