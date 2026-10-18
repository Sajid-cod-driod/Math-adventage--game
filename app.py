import streamlit as st
import random

st.set_page_config(
    page_title="Math Adventure: Learn & Play",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Math Adventure: Learn & Play")
st.subheader("🌟 Learn Mathematics, Play Games, Win Badges!")

st.write(
    "Welcome, young mathematician! "
    "Learn a concept, study examples, and answer questions."
)

LEVELS = {
    1: {
        "name": "🔢 Number Explorer",
        "definition": "A number tells us how many things there are or where something is in a sequence.",
        "example": "Example: 🍎🍎🍎 means 3 apples. Also, 8 is greater than 5.",
        "questions": [
            {
                "q": "Which number is greater?",
                "options": ["3", "7", "2", "1"],
                "answer": "7",
                "hint": "Compare the sizes of the numbers.",
                "explanation": "7 is greater than 3, 2, and 1."
            },
            {
                "q": "What number comes after 9?",
                "options": ["8", "10", "7", "11"],
                "answer": "10",
                "hint": "Count forward: 8, 9, ...",
                "explanation": "After 9 comes 10."
            },
            {
                "q": "How many sides does a triangle have?",
                "options": ["2", "3", "4", "5"],
                "answer": "3",
                "hint": "Count the straight edges.",
                "explanation": "A triangle has 3 sides."
            },
            {
                "q": "Which number is the smallest?",
                "options": ["6", "4", "9", "2"],
                "answer": "2",
                "hint": "Look for the number with the lowest value.",
                "explanation": "2 is smaller than 4, 6, and 9."
            },
            {
                "q": "What is 5 + 0?",
                "options": ["0", "10", "5", "1"],
                "answer": "5",
                "hint": "Adding zero does not change a number.",
                "explanation": "5 + 0 = 5."
            },
            {
                "q": "Which number comes before 6?",
                "options": ["5", "7", "8", "9"],
                "answer": "5",
                "hint": "Count backward from 6.",
                "explanation": "5 comes immediately before 6."
            },
            {
                "q": "How many fingers are on one hand?",
                "options": ["4", "5", "6", "10"],
                "answer": "5",
                "hint": "Count your fingers!",
                "explanation": "One hand usually has 5 fingers."
            },
            {
                "q": "Which is an even number?",
                "options": ["3", "5", "8", "9"],
                "answer": "8",
                "hint": "An even number can be split into two equal groups.",
                "explanation": "8 can be divided into two groups of 4."
            },
            {
                "q": "What number comes after 14?",
                "options": ["13", "15", "16", "12"],
                "answer": "15",
                "hint": "Count one step forward.",
                "explanation": "After 14 comes 15."
            },
            {
                "q": "How many wheels do 2 bicycles have altogether?",
                "options": ["2", "3", "4", "6"],
                "answer": "4",
                "hint": "Each bicycle has 2 wheels.",
                "explanation": "2 bicycles have 2 + 2 = 4 wheels."
            }
        ]
    },

    2: {
        "name": "🏝️ Addition Island",
        "definition": "Addition means putting numbers together to find their total. The symbol is +.",
        "example": "Example: 3 + 2 = 5. Start with 3 and count 2 more: 4, 5.",
        "questions": [
            {
                "q": "What is 2 + 3?",
                "options": ["4", "5", "6", "3"],
                "answer": "5",
                "hint": "Start at 2 and count 3 more.",
                "explanation": "2 + 3 = 5."
            },
            {
                "q": "What is 4 + 4?",
                "options": ["6", "7", "8", "9"],
                "answer": "8",
                "hint": "Double 4.",
                "explanation": "4 + 4 = 8."
            },
            {
                "q": "What is 6 + 2?",
                "options": ["7", "8", "9", "6"],
                "answer": "8",
                "hint": "Count two steps after 6.",
                "explanation": "6 + 2 = 8."
            },
            {
                "q": "You have 3 candies and get 4 more. How many?",
                "options": ["6", "7", "8", "5"],
                "answer": "7",
                "hint": "Put the two groups together.",
                "explanation": "3 + 4 = 7 candies."
            },
            {
                "q": "What is 10 + 5?",
                "options": ["12", "13", "15", "14"],
                "answer": "15",
                "hint": "Start at 10 and count 5 more.",
                "explanation": "10 + 5 = 15."
            },
            {
                "q": "What is 7 + 3?",
                "options": ["9", "10", "11", "8"],
                "answer": "10",
                "hint": "How many more does 7 need to make 10?",
                "explanation": "7 + 3 = 10."
            },
            {
                "q": "What is 5 + 5?",
                "options": ["5", "10", "15", "20"],
                "answer": "10",
                "hint": "Double 5.",
                "explanation": "5 + 5 = 10."
            },
            {
                "q": "What is 8 + 1?",
                "options": ["7", "8", "9", "10"],
                "answer": "9",
                "hint": "Count one number after 8.",
                "explanation": "8 + 1 = 9."
            },
            {
                "q": "What is 12 + 3?",
                "options": ["14", "15", "16", "13"],
                "answer": "15",
                "hint": "Add 3 to 12.",
                "explanation": "12 + 3 = 15."
            },
            {
                "q": "There are 6 red balls and 2 blue balls. How many balls?",
                "options": ["7", "8", "9", "6"],
                "answer": "8",
                "hint": "Add the red and blue balls.",
                "explanation": "6 + 2 = 8 balls."
            }
        ]
    },

    3: {
        "name": "⛰️ Subtraction Mountain",
        "definition": "Subtraction means taking one number away from another. The symbol is −.",
        "example": "Example: 5 − 2 = 3. Start with 5 and take away 2.",
        "questions": [
            {
                "q": "What is 5 − 2?",
                "options": ["2", "3", "4", "5"],
                "answer": "3",
                "hint": "Start at 5 and count backward twice.",
                "explanation": "5 − 2 = 3."
            },
            {
                "q": "What is 9 − 4?",
                "options": ["4", "5", "6", "3"],
                "answer": "5",
                "hint": "Count backward four steps from 9.",
                "explanation": "9 − 4 = 5."
            },
            {
                "q": "What is 7 − 1?",
                "options": ["5", "6", "7", "8"],
                "answer": "6",
                "hint": "Take away one.",
                "explanation": "7 − 1 = 6."
            },
            {
                "q": "You have 8 cookies and eat 3. How many remain?",
                "options": ["4", "5", "6", "3"],
                "answer": "5",
                "hint": "Take 3 away from 8.",
                "explanation": "8 − 3 = 5 cookies."
            },
            {
                "q": "What is 10 − 5?",
                "options": ["4", "5", "6", "3"],
                "answer": "5",
                "hint": "Half of 10 is 5.",
                "explanation": "10 − 5 = 5."
            },
            {
                "q": "What is 12 − 2?",
                "options": ["8", "9", "10", "11"],
                "answer": "10",
                "hint": "Take two away from twelve.",
                "explanation": "12 − 2 = 10."
            },
            {
                "q": "What is 6 − 6?",
                "options": ["0", "1", "6", "12"],
                "answer": "0",
                "hint": "If you take everything away, what remains?",
                "explanation": "6 − 6 = 0."
            },
            {
                "q": "What is 15 − 5?",
                "options": ["5", "10", "15", "20"],
                "answer": "10",
                "hint": "Subtract five from fifteen.",
                "explanation": "15 − 5 = 10."
            },
            {
                "q": "There are 9 birds. 2 fly away. How many remain?",
                "options": ["6", "7", "8", "5"],
                "answer": "7",
                "hint": "Subtract the birds that flew away.",
                "explanation": "9 − 2 = 7 birds."
            },
            {
                "q": "What is 14 − 4?",
                "options": ["8", "9", "10", "11"],
                "answer": "10",
                "hint": "Take away four.",
                "explanation": "14 − 4 = 10."
            }
        ]
    },

    4: {
        "name": "🌴 Multiplication Jungle",
        "definition": "Multiplication is a quick way to add equal groups. The symbol is ×.",
        "example": "Example: 3 × 2 means 3 groups of 2: 2 + 2 + 2 = 6.",
        "questions": [
            {
                "q": "What is 2 × 3?",
                "options": ["5", "6", "8", "9"],
                "answer": "6",
                "hint": "Add 3 + 3.",
                "explanation": "2 × 3 = 3 + 3 = 6."
            },
            {
                "q": "What is 4 × 2?",
                "options": ["6", "8", "10", "4"],
                "answer": "8",
                "hint": "Add 2 four times.",
                "explanation": "4 × 2 = 2 + 2 + 2 + 2 = 8."
            },
            {
                "q": "What is 5 × 5?",
                "options": ["10", "20", "25", "30"],
                "answer": "25",
                "hint": "Five groups of five.",
                "explanation": "5 × 5 = 25."
            },
            {
                "q": "What is 3 × 4?",
                "options": ["7", "12", "9", "16"],
                "answer": "12",
                "hint": "Add 4 + 4 + 4.",
                "explanation": "3 × 4 = 12."
            },
            {
                "q": "What is 10 × 2?",
                "options": ["10", "12", "20", "22"],
                "answer": "20",
                "hint": "Double 10.",
                "explanation": "10 × 2 = 20."
            },
            {
                "q": "What is 6 × 2?",
                "options": ["8", "10", "12", "14"],
                "answer": "12",
                "hint": "Double 6.",
                "explanation": "6 × 2 = 12."
            },
            {
                "q": "What is 3 × 3?",
                "options": ["6", "9", "12", "3"],
                "answer": "9",
                "hint": "Add 3 + 3 + 3.",
                "explanation": "3 × 3 = 9."
            },
            {
                "q": "Four bags contain 2 apples each. How many apples?",
                "options": ["6", "8", "10", "4"],
                "answer": "8",
                "hint": "Multiply 4 bags by 2 apples.",
                "explanation": "4 × 2 = 8 apples."
            },
            {
                "q": "What is 5 × 2?",
                "options": ["7", "10", "12", "15"],
                "answer": "10",
                "hint": "Count by twos five times.",
                "explanation": "5 × 2 = 10."
            },
            {
                "q": "What is 2 × 6?",
                "options": ["8", "10", "12", "14"],
                "answer": "12",
                "hint": "Double 6.",
                "explanation": "2 × 6 = 12."
            }
        ]
    },

    5: {
        "name": "🪐 Division Planet",
        "definition": "Division means sharing equally or splitting into equal groups. The symbol is ÷.",
        "example": "Example: 6 ÷ 2 = 3. Six apples shared equally by two children gives each child 3.",
        "questions": [
            {
                "q": "What is 6 ÷ 2?",
                "options": ["2", "3", "4", "6"],
                "answer": "3",
                "hint": "Share six equally between two groups.",
                "explanation": "6 ÷ 2 = 3."
            },
            {
                "q": "What is 8 ÷ 2?",
                "options": ["2", "3", "4", "6"],
                "answer": "4",
                "hint": "Split eight into two equal groups.",
                "explanation": "8 ÷ 2 = 4."
            },
            {
                "q": "What is 10 ÷ 5?",
                "options": ["1", "2", "5", "10"],
                "answer": "2",
                "hint": "How many fives make ten?",
                "explanation": "10 ÷ 5 = 2."
            },
            {
                "q": "What is 12 ÷ 3?",
                "options": ["3", "4", "5", "6"],
                "answer": "4",
                "hint": "How many groups of three make twelve?",
                "explanation": "12 ÷ 3 = 4."
            },
            {
                "q": "Share 8 candies equally among 4 children. Each gets?",
                "options": ["1", "2", "3", "4"],
                "answer": "2",
                "hint": "Divide 8 by 4.",
                "explanation": "8 ÷ 4 = 2 candies per child."
            },
            {
                "q": "What is 15 ÷ 3?",
                "options": ["3", "4", "5", "6"],
                "answer": "5",
                "hint": "Count by threes until you reach fifteen.",
                "explanation": "15 ÷ 3 = 5."
            },
            {
                "q": "What is 20 ÷ 2?",
                "options": ["5", "10", "15", "20"],
                "answer": "10",
                "hint": "Half of twenty.",
                "explanation": "20 ÷ 2 = 10."
            },
            {
                "q": "What is 9 ÷ 3?",
                "options": ["2", "3", "4", "6"],
                "answer": "3",
                "hint": "How many threes make nine?",
                "explanation": "9 ÷ 3 = 3."
            },
            {
                "q": "What is 16 ÷ 4?",
                "options": ["2", "3", "4", "8"],
                "answer": "4",
                "hint": "How many fours make sixteen?",
                "explanation": "16 ÷ 4 = 4."
            },
            {
                "q": "Ten toys are shared by two children equally. Each gets?",
                "options": ["2", "4", "5", "8"],
                "answer": "5",
                "hint": "Divide ten by two.",
                "explanation": "10 ÷ 2 = 5 toys each."
            }
        ]
    },

    6: {
        "name": "🍕 Fractions World",
        "definition": "A fraction shows equal parts of a whole. The top number is the numerator, and the bottom number is the denominator.",
        "example": "Example: If a pizza is cut into 4 equal pieces and you eat 1, you ate 1/4.",
        "questions": [
            {
                "q": "A pizza has 4 equal slices. You eat 1. What fraction did you eat?",
                "options": ["1/2", "1/3", "1/4", "4/1"],
                "answer": "1/4",
                "hint": "One slice out of four equal slices.",
                "explanation": "You ate 1 out of 4 equal pieces: 1/4."
            },
            {
                "q": "What is half of 8?",
                "options": ["2", "3", "4", "6"],
                "answer": "4",
                "hint": "Split 8 into two equal groups.",
                "explanation": "8 ÷ 2 = 4."
            },
            {
                "q": "Which fraction means one half?",
                "options": ["1/2", "1/3", "1/4", "2/3"],
                "answer": "1/2",
                "hint": "One part out of two equal parts.",
                "explanation": "1/2 means one of two equal parts."
            },
            {
                "q": "A cake is cut into 3 equal pieces. You take 1. What fraction?",
                "options": ["1/2", "1/3", "2/3", "3/1"],
                "answer": "1/3",
                "hint": "One piece out of three.",
                "explanation": "One out of three equal pieces is 1/3."
            },
            {
                "q": "How many halves make one whole?",
                "options": ["1", "2", "3", "4"],
                "answer": "2",
                "hint": "Think of splitting a whole into two equal parts.",
                "explanation": "Two halves make one whole."
            },
            {
                "q": "Which is larger: 1/2 or 1/4?",
                "options": ["1/2", "1/4", "They are equal", "Cannot tell"],
                "answer": "1/2",
                "hint": "Imagine the same pizza divided into 2 pieces or 4 pieces.",
                "explanation": "One half is larger than one quarter of the same whole."
            },
            {
                "q": "How many quarters make one whole?",
                "options": ["2", "3", "4", "5"],
                "answer": "4",
                "hint": "A quarter is one of four equal parts.",
                "explanation": "Four quarters make one whole."
            },
            {
                "q": "What is one half of 10?",
                "options": ["2", "4", "5", "10"],
                "answer": "5",
                "hint": "Divide ten by two.",
                "explanation": "10 ÷ 2 = 5."
            },
            {
                "q": "In the fraction 3/5, what is the top number?",
                "options": ["3", "5", "8", "2"],
                "answer": "3",
                "hint": "The top number is called the numerator.",
                "explanation": "In 3/5, the numerator is 3."
            },
            {
                "q": "In the fraction 2/7, what is the bottom number?",
                "options": ["2", "5", "7", "9"],
                "answer": "7",
                "hint": "The bottom number is called the denominator.",
                "explanation": "In 2/7, the denominator is 7."
            }
        ]
    },

    7: {
        "name": "📐 Geometry Kingdom",
        "definition": "Geometry is the study of shapes, sizes, lines, and positions.",
        "example": "Example: A triangle has 3 sides. A square has 4 equal sides.",
        "questions": [
            {
                "q": "How many sides does a square have?",
                "options": ["3", "4", "5", "6"],
                "answer": "4",
                "hint": "Count the edges of a square.",
                "explanation": "A square has 4 equal sides."
            },
            {
                "q": "How many corners does a rectangle have?",
                "options": ["2", "3", "4", "5"],
                "answer": "4",
                "hint": "Count its vertices.",
                "explanation": "A rectangle has 4 corners."
            },
            {
                "q": "Which shape is round and has no corners?",
                "options": ["Triangle", "Square", "Circle", "Rectangle"],
                "answer": "Circle",
                "hint": "Think of a coin.",
                "explanation": "A circle is round and has no corners."
            },
            {
                "q": "How many sides does a pentagon have?",
                "options": ["4", "5", "6", "7"],
                "answer": "5",
                "hint": "Penta means five.",
                "explanation": "A pentagon has 5 sides."
            },
            {
                "q": "How many sides does a hexagon have?",
                "options": ["4", "5", "6", "8"],
                "answer": "6",
                "hint": "Think of a six-sided shape.",
                "explanation": "A hexagon has 6 sides."
            },
            {
                "q": "Which shape has 3 sides?",
                "options": ["Circle", "Triangle", "Square", "Hexagon"],
                "answer": "Triangle",
                "hint": "Tri means three.",
                "explanation": "A triangle has 3 sides."
            },
            {
                "q": "How many equal sides does a square have?",
                "options": ["2", "3", "4", "5"],
                "answer": "4",
                "hint": "All sides of a square are equal.",
                "explanation": "A square has four equal sides."
            },
            {
                "q": "Which object is shaped most like a sphere?",
                "options": ["Book", "Ball", "Door", "Plate"],
                "answer": "Ball",
                "hint": "Think of a round 3D object.",
                "explanation": "A ball is approximately spherical."
            },
            {
                "q": "How many corners does a triangle have?",
                "options": ["2", "3", "4", "5"],
                "answer": "3",
                "hint": "Each pair of sides meets at a corner.",
                "explanation": "A triangle has 3 corners."
            },
            {
                "q": "Which shape has 4 sides?",
                "options": ["Triangle", "Square", "Pentagon", "Hexagon"],
                "answer": "Square",
                "hint": "Count the sides.",
                "explanation": "A square has 4 sides."
            }
        ]
    },

    8: {
        "name": "⏰ Time Master",
        "definition": "Time tells us when something happens and how long it lasts. We measure it in seconds, minutes, and hours.",
        "example": "Example: 60 minutes make 1 hour.",
        "questions": [
            {
                "q": "How many minutes are in one hour?",
                "options": ["30", "45", "60", "100"],
                "answer": "60",
                "hint": "Remember: one hour has sixty minutes.",
                "explanation": "1 hour = 60 minutes."
            },
            {
                "q": "How many days are in one week?",
                "options": ["5", "6", "7", "8"],
                "answer": "7",
                "hint": "Count Monday through Sunday.",
                "explanation": "One week has 7 days."
            },
            {
                "q": "Which day comes after Monday?",
                "options": ["Sunday", "Tuesday", "Wednesday", "Friday"],
                "answer": "Tuesday",
                "hint": "Think of the days of the week.",
                "explanation": "Tuesday comes after Monday."
            },
            {
                "q": "How many months are in one year?",
                "options": ["10", "11", "12", "13"],
                "answer": "12",
                "hint": "January through December.",
                "explanation": "One year has 12 months."
            },
            {
                "q": "What time is 1 hour after 3:00?",
                "options": ["2:00", "3:30", "4:00", "5:00"],
                "answer": "4:00",
                "hint": "Move forward one hour.",
                "explanation": "One hour after 3:00 is 4:00."
            },
            {
                "q": "How many seconds are in one minute?",
                "options": ["30", "45", "60", "100"],
                "answer": "60",
                "hint": "A minute has sixty seconds.",
                "explanation": "1 minute = 60 seconds."
            },
            {
                "q": "Which month comes after March?",
                "options": ["February", "April", "May", "June"],
                "answer": "April",
                "hint": "Remember the order of the months.",
                "explanation": "April comes after March."
            },
            {
                "q": "What time is half past 2?",
                "options": ["2:15", "2:30", "3:00", "1:30"],
                "answer": "2:30",
                "hint": "Half an hour is 30 minutes.",
                "explanation": "Half past 2 means 2:30."
            },
            {
                "q": "How many days are in a non-leap year?",
                "options": ["300", "360", "365", "366"],
                "answer": "365",
                "hint": "Most years have 365 days.",
                "explanation": "A non-leap year has 365 days."
            },
            {
                "q": "What time is 30 minutes after 5:00?",
                "options": ["5:15", "5:30", "6:00", "4:30"],
                "answer": "5:30",
                "hint": "Add half an hour.",
                "explanation": "30 minutes after 5:00 is 5:30."
            }
        ]
    },

    9: {
        "name": "💰 Money Mission",
        "definition": "Money is used to buy things. We can add and subtract money to find totals and change.",
        "example": "Example: €2 + €3 = €5.",
        "questions": [
            {
                "q": "What is €2 + €3?",
                "options": ["€4", "€5", "€6", "€1"],
                "answer": "€5",
                "hint": "Add two euros and three euros.",
                "explanation": "€2 + €3 = €5."
            },
            {
                "q": "You have €10 and spend €4. How much remains?",
                "options": ["€4", "€5", "€6", "€7"],
                "answer": "€6",
                "hint": "Subtract four from ten.",
                "explanation": "€10 − €4 = €6."
            },
            {
                "q": "Which amount is greater?",
                "options": ["€1", "€2", "€5", "€0.50"],
                "answer": "€5",
                "hint": "Compare the values.",
                "explanation": "€5 is greater than the other amounts."
            },
            {
                "q": "A toy costs €3. You pay €5. How much change?",
                "options": ["€1", "€2", "€3", "€5"],
                "answer": "€2",
                "hint": "Subtract the price from the amount paid.",
                "explanation": "€5 − €3 = €2 change."
            },
            {
                "q": "What is €1 + €1 + €1?",
                "options": ["€2", "€3", "€4", "€1"],
                "answer": "€3",
                "hint": "Add three one-euro coins.",
                "explanation": "€1 + €1 + €1 = €3."
            },
            {
                "q": "Two items cost €4 each. What is the total?",
                "options": ["€4", "€6", "€8", "€10"],
                "answer": "€8",
                "hint": "Add €4 twice.",
                "explanation": "€4 + €4 = €8."
            },
            {
                "q": "You have €7. You buy a book for €2. How much remains?",
                "options": ["€3", "€4", "€5", "€6"],
                "answer": "€5",
                "hint": "Subtract the cost of the book.",
                "explanation": "€7 − €2 = €5."
            },
            {
                "q": "Which is equal to 100 cents?",
                "options": ["€0.10", "€0.50", "€1", "€2"],
                "answer": "€1",
                "hint": "One euro contains one hundred cents.",
                "explanation": "100 cents = €1."
            },
            {
                "q": "An apple costs €2 and a banana costs €1. Total?",
                "options": ["€1", "€2", "€3", "€4"],
                "answer": "€3",
                "hint": "Add the two prices.",
                "explanation": "€2 + €1 = €3."
            },
            {
                "q": "You pay €10 for something costing €6. Change?",
                "options": ["€2", "€3", "€4", "€6"],
                "answer": "€4",
                "hint": "Find 10 minus 6.",
                "explanation": "€10 − €6 = €4."
            }
        ]
    },

    10: {
        "name": "🏆 Math Champion",
        "definition": "A Math Champion uses different math skills to solve problems carefully.",
        "example": "Example: If you have 3 bags with 2 apples each, you have 3 × 2 = 6 apples.",
        "questions": [
            {
                "q": "What is 7 + 8?",
                "options": ["13", "14", "15", "16"],
                "answer": "15",
                "hint": "Make 10 first: 7 + 3 + 5.",
                "explanation": "7 + 8 = 15."
            },
            {
                "q": "What is 20 − 7?",
                "options": ["11", "12", "13", "14"],
                "answer": "13",
                "hint": "Take away seven from twenty.",
                "explanation": "20 − 7 = 13."
            },
            {
                "q": "What is 4 × 3?",
                "options": ["7", "12", "16", "9"],
                "answer": "12",
                "hint": "Add 3 four times.",
                "explanation": "4 × 3 = 12."
            },
            {
                "q": "What is 18 ÷ 3?",
                "options": ["3", "5", "6", "9"],
                "answer": "6",
                "hint": "How many threes make eighteen?",
                "explanation": "18 ÷ 3 = 6."
            },
            {
                "q": "What is half of 12?",
                "options": ["4", "5", "6", "8"],
                "answer": "6",
                "hint": "Divide twelve into two equal groups.",
                "explanation": "12 ÷ 2 = 6."
            },
            {
                "q": "How many sides does a hexagon have?",
                "options": ["4", "5", "6", "8"],
                "answer": "6",
                "hint": "Hex means six.",
                "explanation": "A hexagon has six sides."
            },
            {
                "q": "What is 30 minutes after 2:00?",
                "options": ["2:15", "2:30", "3:00", "3:30"],
                "answer": "2:30",
                "hint": "Add half an hour.",
                "explanation": "30 minutes after 2:00 is 2:30."
            },
            {
                "q": "You have €5 and earn €3. How much do you have?",
                "options": ["€2", "€5", "€8", "€15"],
                "answer": "€8",
                "hint": "Add five and three.",
                "explanation": "€5 + €3 = €8."
            },
            {
                "q": "What is 9 + 9?",
                "options": ["16", "17", "18", "19"],
                "answer": "18",
                "hint": "Double nine.",
                "explanation": "9 + 9 = 18."
            },
            {
                "q": "There are 4 children with 3 balloons each. How many balloons?",
                "options": ["7", "10", "12", "14"],
                "answer": "12",
                "hint": "Multiply 4 by 3.",
                "explanation": "4 × 3 = 12 balloons."
            }
        ]
    }
}

st.success("The 10 learning levels and their questions are ready!")
st.write("Total questions:", sum(len(level["questions"]) for level in LEVELS.values()))


import streamlit as st


st.title("🎮 Math Adventure: Learn & Play")
st.write("Learn first, then play and earn points!")

if "unlocked_level" not in st.session_state:
    st.session_state.unlocked_level = 1

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

if "level_scores" not in st.session_state:
    st.session_state.level_scores = {}

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "level" not in st.session_state:
    st.session_state.level = 1

level_number = st.session_state.level
level_data = LEVELS[level_number]
questions = level_data["questions"]

st.sidebar.header("🗺️ Choose Your Adventure")

available_levels = list(
    range(1, st.session_state.unlocked_level + 1)
)

selected_level = st.sidebar.selectbox(
    "Choose an unlocked level",
    available_levels,
    format_func=lambda x: f"Level {x}: {LEVELS[x]['name']}",
    index=available_levels.index(level_number)
    if level_number in available_levels else 0
)

if selected_level != level_number:
    st.session_state.level = selected_level
    st.session_state.question_index = 0
    st.session_state.submitted = False
    st.rerun()

st.sidebar.metric("⭐ Total Score", st.session_state.total_score)

st.header(f"Level {level_number}: {level_data['name']}")

st.subheader("📚 Learn the Definition")
st.info(level_data["definition"])

st.subheader("💡 Example")
st.write(level_data["example"])

st.divider()

index = st.session_state.question_index

if index < len(questions):
    question = questions[index]

    st.progress((index + 1) / len(questions))
    st.write(f"Question {index + 1} of {len(questions)}")

    st.subheader("❓ " + question["q"])

    answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"answer_{level_number}_{index}"
    )

    if st.button("💡 Show Hint"):
        st.warning("Hint: " + question["hint"])

    if not st.session_state.submitted:
        if st.button("✅ Submit Answer"):
            st.session_state.submitted = True

            if answer == question["answer"]:
                st.session_state.total_score += 10

                st.session_state.level_scores[level_number] = (
                    st.session_state.level_scores.get(level_number, 0) + 10
                )

                st.session_state[f"correct_{level_number}_{index}"] = True
            else:
                st.session_state[f"correct_{level_number}_{index}"] = False

            st.rerun()

    else:
        correct = st.session_state.get(
            f"correct_{level_number}_{index}", False
        )

        if correct:
            st.success("🎉 Excellent! Correct answer! You earned 10 points.")
        else:
            st.error("Not quite! Let's learn together.")
            st.write("Your answer:", answer)
            st.write("Correct answer:", question["answer"])

        st.info("📖 Explanation: " + question["explanation"])

        if st.button("➡️ Next Question"):
            st.session_state.question_index += 1
            st.session_state.submitted = False
            st.rerun()

else:
    st.balloons()
    st.success(f"🏆 You completed Level {level_number}!")

    level_score = st.session_state.level_scores.get(level_number, 0)

    st.metric("Points earned in this level", level_score)
    st.metric("Total points", st.session_state.total_score)

    st.write("🌟 Great work! Keep learning and practicing.")

    if level_number < len(LEVELS):
        if st.button("🔓 Unlock Next Level"):
            st.session_state.unlocked_level = max(
                st.session_state.unlocked_level,
                level_number + 1
            )
            st.session_state.level = level_number + 1
            st.session_state.question_index = 0
            st.session_state.submitted = False
            st.rerun()

    if st.button("🔄 Restart This Level"):
        st.session_state.question_index = 0
        st.session_state.submitted = False
        st.rerun()
