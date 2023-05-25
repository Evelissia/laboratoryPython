from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# декоратор для POST-запросов. Когда пользователь отправляет форму на этот адрес, вызывается функция calculate()
@app.route('/calculate', methods=['POST'])

# функция обработчик для страницы расчета
def calculate():
    loan_amount = float(request.form['loan_amount'])
    interest_rate = float(request.form['interest_rate'])
    loan_term = int(request.form['loan_term'])
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)
    total_payment = monthly_payment * loan_term
    return render_template('result.html', monthly_payment=monthly_payment, total_payment=total_payment)

# функция для расчета ежемесячного платежа
def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    
    if loan_amount < 0:
        raise ValueError("Loan amount must be a positive value.")
    
    if interest_rate == 0.0:
        return 0.0
    
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment

if __name__ == '__main__':
    app.run(debug=True)