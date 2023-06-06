var flashcards = document.querySelectorAll('.flashcard');


const inputs = document.querySelectorAll('input[type="number"]');
inputs.forEach(input => input.addEventListener('input', calculateGPA));
flashcards.forEach(function(flashcard) {
	flashcard.addEventListener('click', function() {
		flashcard.classList.toggle('flashcard--flipped');
	});
});
flashcards.forEach(function(flashcard) {

	var buttonNext = flashcard.querySelector('.flashcard__next');
	var buttonPrev = flashcard.querySelector('.flashcard__previous');
	var numbers = flashcard.querySelector('.flashcard__numb');
	var term = flashcard.querySelector('.flashcard__term');
	var definition = flashcard.querySelector('.flashcard__definition');
	var currentIndex = 0;
	var data = [
		{
			numbers: '1/20',
			term: 'Academic freedom!',
			definition: 'is a set of powers of subjects of educational the process provided by them for self-determination of the content education in the disciplines of the component of choice, additional types of education and organization of educational activities in order to create conditions for creative development of students, teachers and application of innovative technologies and teaching methods;'
		},
		{
			numbers: '2/20',
			term: 'Question 2',
			definition: 'AKwODa awdawdwadwa dawdawd wadawdawda wdawdawdawdawdaw'
		},
		{
			numbers: '3/20',
			term: 'Question 3',
			definition: 'Answer 3'
		},
		{
			numbers: '4/20',
			term: 'Question 4',
			definition: 'Answer 4'
		},
		{
			numbers: '5/20',
			term: 'Question 5',
			definition: 'Answer 5'
		}
	];
	
	buttonNext.addEventListener('click', function() {
			flashcard.classList.remove('flashcard--flipped');
			
		
		flashcard.classList.toggle('flashcard--flipped');
			term.textContent = '';
			currentIndex = (currentIndex + 1) % data.length;
			setTimeout(function() {
				definition.textContent = data[currentIndex].definition;
			}, 250);
			term.textContent = data[currentIndex].term;
			numbers.textContent = data[currentIndex].numbers;
	});

	buttonPrev.addEventListener('click', function() {
			flashcard.classList.remove('flashcard--flipped');
		
		flashcard.classList.toggle('flashcard--flipped');
			term.textContent = '';
			if(currentIndex == 0){
				currentIndex = data.length;
			}	
			currentIndex = (currentIndex - 1) % data.length;
				setTimeout(function() {
					definition.textContent = data[currentIndex].definition;
				}, 250);
				term.textContent = data[currentIndex].term;
				numbers.textContent = data[currentIndex].numbers;
			
	});

});


