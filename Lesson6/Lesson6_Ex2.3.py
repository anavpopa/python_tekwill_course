email=input('Introduce email address')
parts=email.split('@')
if len(parts)!=2 or len(parts[0])==0:
    print('Not valid')
else:
    domain=parts[1].split('.')
    if len(domain)!=2:
        print('Not valid')
    else:
        print('Valid')


    
    