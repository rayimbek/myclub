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
			numbers: '1/15',
			term: 'SEB',
			definition: 'Safe Exam Browser'
		},
		{
			numbers: '2/15',
			term: 'Moodle',
			definition: 'Main Platform'
		},
		{
			numbers: '3/15',
			term: 'SIS',
			definition: 'Student Independent study'
		},
		{
			numbers: '4/15',
			term: 'Midterm',
			definition: 'Firt attestation exam'
		},
		{
			numbers: '5/15',
			term: 'Endterm',
			definition: 'Second attestation exam'
		},
		{
			numbers: '6/15',
			term: 'Academic freedom!',
			definition: 'is a set of powers of subjects of educational the process provided by them for self-determination of the content education in the disciplines of the component of choice, additional types of education and organization of educational activities in order to create conditions for creative development of students, teachers and application of innovative technologies and teaching methods;'
		},
		{
			numbers: '7/15',
			term: 'Academic credit',
			definition: 'unified unit of measurement of scientific and(or) educational work (load) of the student and (or) teacher;'
		},
		{
			numbers: '8/15',
			term: 'Academic mobility',
			definition: 'movement of students or teachers-researchers to teach or conduct research on a specificacademic period (semester or academic year) to another university (within the country or outside abroad) with obligatory transfer of mastered curricula, disciplines in the form academic credits at your university or to continue your studies at another university;'
		},
		{
			numbers: '9/15',
			term: 'Double Degree Education',
			definition: 'the opportunity to study in two educational programs and curricula in order to obtain two equivalent diplomas or one main and the second additional;'
		},
		{
			numbers: '10/15',
			term: 'Individual curriculum',
			definition: 'curriculum for each academic year for students on their own with the help of an advisor based on educational program and catalog of elective disciplines and (or) modules;'
		},
		{
			numbers: '11/15',
			term: 'Grade Point Average (GPA)',
			definition: 'weighted average assessment of the level of educational achievements of the student for a certain period according to selected program (the ratio of the sum of the products of credits on digital the equivalent of the points of the final assessment for all types of educational work to the total number credits for these types of work for a given period of study);'
		},
		{
			numbers: '12/15',
			term: 'Transcript',
			definition: 'a document containing a list of mastered disciplines and (or) modules, and other types of educational work for the corresponding period of study with indication of credits and grades;'
		},
		{
			numbers: '13/15',
			term: 'Advisor',
			definition: 'teacher performing the functions of an academic mentor of the student in the relevant educational program, assisting in choosing a learning path (formation individual curriculum) and the development of the educational program during the period learning.'
		},
		{
			numbers: '14/15',
			term: 'Elective disciplines',
			definition: 'academic disciplines included in the university component and an elective component within established academic credits and introductory educational organizations reflecting the individual training of the student, taking into account the specifics of socio-economic development and the needs specific region, established scientific schools;'
		},
		{
			numbers: '15/15',
			term: 'Educational portal',
			definition: 'system-organized, interconnected a set of information resources and services on the Internet, containing administrative-academic and educational-methodical information, allowing organize the educational process for distance learning technologies'
		},
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


