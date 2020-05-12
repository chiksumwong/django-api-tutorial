import requests


def list_calendars(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == '__main__':
    input_access_token = "EwBwA8l6BAAUO9chh8cJscQLmU LSWpbnr0vmwwAATGIqi4Saeq2f1nbvFmjm64gF2iWe3uWB7QeP 4zhuJuHz3ASvaAy7oUvHByQm5DoTCPsPBxspLNyzJNgHjDx9Tr HA50UW5rDY/D3VyOcQWoT2Tqx7apLX1PZ0PjS9FPBesdiZSbl5rmRfazZLzRShBEt/3VJO4AoRqz0omX2xYmC3o5oNI39ZJkpZxdFqyi2ietuC3SCa/x2/vaBydzqVm8 WObOe9t00NTt1 scdawM20KKSYbwDHaGdJuevzUIY7QN2TLJvIwDNCyWffP9hlomB4KB3QSTJSUEdllDZe7Oazhpuar/4zQHP2cY6uwuMSJn3IlhT970ccU71gC58DZgAACJCswHq5f2QqQAIqokCM9iRXvxO/Hr8EfD / qYjZfE 1zGjhHKvK/vzg0U1PbAZHE1gVGlyvh5Ucp0LHL7ODdqo0PLt4S3/PYIYoaaN8bEkMUHXnEzgOSIArA9bha2xkEYQ7sR1m YiK9i027ig0TBSjMhO01jR3md7vNfBDUEpuCHgn4LPrsFtiwego1SyoMbGeqc/IMVky9Kf/4PwmI4NAYysQ6DHscfSbVgmk GOzDgQVWoYRWrJwE26wTsVsPimeaonc9iKYB0xRwekGwtyaOumjcBHc5EmolOqJJGyJo7cwZUrO7ilb8 yvT/kGD47dBWaadeb0PfDB0cYUrBAfoAr e/FvLZnpTFohULYypMIEtppTP J7UJTTsVmk4utZ9YlFAVU8wIgFDa7OiU9Lnw0Rdp3DFePIq/hsiSV0G961Q1CbOm2d8xjKfsQsWJYP2BMlh/YQ60lcAxXO7hgtHG BmnVsZzdHtu2Ievcn6VnxHumEMgKC4EzS5 YJlS1O4wzUzbkDBSWrhFH PApWep5G HwHX0RmhupBv wPUlDX37QNDDtgxI5dzLQPpHPOHyRa2jeZWajgDTRaSPIgjsBSw77WOrVW8Fu/k/smlc/xHf2gNTBAElQY8nsWYxv1huxKbX 1AOfVPAm9n2xWyfaI/YCda6fr7QCuqwaB7RB/lpCyCQtUNtBLUDgPwLvRtHaLGK10tHFzaMnelFuE16xzR8Y5BLFv29FIroEqrxYYU5LRKKeLvWxvGZA7QRj4/OTL27hCu6FAg=="
    print(list_calendars(input_access_token))
