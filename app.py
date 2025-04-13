from carbon_wallet_flask import create_app
app = create_app()
print('run')
if __name__ == '__main__':
   app.run(debug=True)