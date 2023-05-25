def check_credentials(credentials):
    valid_credentials = {
        'Vika Vika': 'Учетные данные верны.',
        'John Doe': 'Учетные данные верны.',
        'Jane Smith': 'Учетные данные верны.',
        'Alice Johnson': 'Учетные данные верны.',
        'Bob Smith': 'Учетные данные верны.',
        'Emma Thompson': 'Учетные данные верны.'
    }

    if credentials in valid_credentials:
        return valid_credentials[credentials]
    else:
        return 'Неверные учетные данные.'