import uuid

ASSIGN_QUIZ_RESPONSE = "Quiz assigned successfully"
CALC_ACCUM_SCORE_RESPONSE = "Accumulated score calculated successfully"
SOLVE_QUESTION_RESPONSE = "Question solved successfully"
QUIZ_ASSIGNMENT_DENIED_TEXT = "You can only assign a quiz that you created"


class Group:
    """
    Group represents the class in which students are and that teachers
    teach. This was used due to Class being conflicting with python
    class keyword.
    """

    def __init__(self, name):
        self.id = int(uuid.uuid4())
        self.name = name


class Student:
    instances = []

    def __init__(self, name, group_id):
        self.id = int(uuid.uuid4())
        self.group_id = group_id
        self.name = name
        self.assigned_quiz = None
        self.accumulated_score = 0
        self.finished_quizzes = []
        # Append all class instances to the instances class variable
        self.__class__.instances.append(self)

    def solve_question(self, question_id, answer):
        """
        This function assumes that all questions are displayed on a page and
        its only called the a user submits an answer to a question.
        """
        questions = self.assigned_quiz.questions
        question = _get_instance(questions, question_id)
        question.given_answer = answer
        answer = question.get_answer()
        given_answer = question.given_answer
        passed = self.check_answer(answer, given_answer)
        question.passed = passed
        question.attempted = True
        unattempted_questions = [
            question for question in questions if question.attempted == False]
        # Check if all questions have been answered
        if len(unattempted_questions) == 0:
            self.assigned_quiz.completed = True
            # Grade score only when all questions have been answered
            self.assigned_quiz.score = self.grade_quiz()
        return SOLVE_QUESTION_RESPONSE

    def check_answer(self, answer, given_answer):
        """Check if the selected choice is right or wrong"""
        passed = False
        for item in answer:
            if len(answer) != len(given_answer):
                return False
            elif item in given_answer:
                passed = True
            else:
                passed = False
        return passed

    def grade_quiz(self):
        """Grade quiz"""
        score = 0
        for question in self.assigned_quiz.questions:
            if question.passed == True:
                score += 1
        return score


class Teacher:
    def __init__(self, name, group_id):
        self.id = int(uuid.uuid4())
        self.name = name
        self.group_id = group_id

    def assign_quiz(self, quiz_id, student_id):
        """Only the quiz author is allowed to assign a quiz to the student."""
        quiz = _get_instance(Quiz.instances, quiz_id)
        if(self.id != quiz.author):
            return QUIZ_ASSIGNMENT_DENIED_TEXT
        student = _get_instance(Student.instances, student_id)
        student.assigned_quiz = quiz
        return ASSIGN_QUIZ_RESPONSE

    def calc_accum_score(self, student_id):
        """Calculate the accumulated score"""
        students = Student.instances
        student = _get_instance(Student.instances, student_id)
        student.accumulated_score += student.assigned_quiz.score
        student.finished_quizzes.append(student.assigned_quiz)
        student.assigned_quiz = None
        return CALC_ACCUM_SCORE_RESPONSE


class Quiz:
    instances = []

    def __init__(self, name, questions,  author, completed=False):
        self.id = int(uuid.uuid4())
        self.name = name
        self.questions = questions
        self.completed = completed
        self.author = author
        self.score = 0
        self.__class__.instances.append(self)

    def add_question(self, question):
        self.questions.append(question)

    def get_quiz(self, id):
        return _get_instance(self.instances)

    def get_quizzes(self):
        return self.instances


class Question:
    def __init__(self, question, choices, answer):
        self.id = int(uuid.uuid4())
        self.question = question
        self.choices = choices
        self.__correct_answer = answer
        self.given_answer = None
        self.passed = False
        self.attempted = False

    def get_answer(self):
        return self.__correct_answer


def _get_instance(list, id):
    """Get instance by id"""
    instance = [instance for instance in list if instance.id == id]
    if(len(instance) == 0):
        raise Exception("Instance does not exist")
    return instance[0]
