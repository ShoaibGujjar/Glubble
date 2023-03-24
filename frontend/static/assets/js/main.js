// const params = new URLSearchParams(window.location.search)

function signIn(event) {

    event.preventDefault()
    email = $("#email").val()
    password = $("#password").val()

    if (email == '' && password == '') {
        showToast("Email and password must be provided!")
        return
    }

    $.ajax({
    type: "post",
    url: "https://oneigsl.com/customer/login/v1/",
    headers: {
        "Content-Type": "application/json"
    },
    data: JSON.stringify({
        "email": email,
        "password": password
    }),

    success: function (data, text) {
        showToast('Success, redirecting you to dashboard..')
        window.localStorage.setItem('customer_id', data.id)
        window.localStorage.setItem('jwt_token', data.jwt_token)
        window.localStorage.setItem('email', data.email)
        window.localStorage.setItem('name', `${data.first_name} ${data.last_name}`)
        window.localStorage.setItem('initials', data.initials)
        window.location.replace('index.php')

    },
    error: function (request, status, error) {
    console.log(error, status)
    if (request.status == 409) {
        showToast(request.responseJSON.detail)
    }
    else {
      showToast(request.responseText)
    }
    }
});
}


function signUp(event) {

    event.preventDefault()
    first_name = $("#f-name").val()
    last_name = $("#l-name").val()
    email = $("#email").val()
    phone_number = $("#contact").val()
    country = $("#country").val()
    state = $("#state").val()
    city = $("#city").val()
    zip_code = $("#zip").val()
    street_address = $("#address").val()
    password = $("#password").val()
    confirm_password = $("#c-password").val()
    // activation_key = params.get('token')

    if (password != confirm_password) {
        showToast("Passwords doesn't match!")
        return
    }

    if (email == '' && password == '') {
        showToast("Email and password must be provided!")
        return
    }

    $.ajax({
    type: "post",
    url: "https://oneigsl.com/customer/register/v1/",
    headers: {
        "Content-Type": "application/json"
    },
    data: JSON.stringify({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "country": country,
        "state": state,
        "city": city,
        "zip_code": zip_code,
        "street_address": street_address,
        "password": password
    }),

    success: function (data, text) {
        showToast('Success, you can sign-in now...')
        window.location.replace('sign-in.php')

    },
    error: function (request, status, error) {
    console.log(error, status)
    if (request.status == 409) {
        showToast(request.responseJSON.detail)
    }
    else {
      showToast(request.responseText)
    }
    }
});
}


function userInfo(info_type) {

    $.ajax({
        type: 'GET',
        url: 'https://oneigsl.com/customer/settings/v1/',
        headers: {
            "Authorization": "Bearer " + window.localStorage.getItem('jwt_token')
        },
        success: function (response) {

            if(info_type == 'personal'){
                document.getElementById('f-name').value = response['first_name'];
                document.getElementById('l-name').value = response['last_name'];
            }
            else{
                document.getElementById('y-name').value = response['first_name'] + ' ' + response['last_name'];
            }

            document.getElementById('email').value = response['email_address'];
            document.getElementById('contact').value = response['phone_number'];
            document.getElementById('country').value = response['country'];
            document.getElementById('state').value = response['state'];
            document.getElementById('city').value = response['city'];
            document.getElementById('zip').value = response['zip_code'];
            document.getElementById('address').value = response['street_address'];
            
        }
    });

}


function updateUserInfo(event) {

    event.preventDefault()
    first_name = $("#f-name").val()
    last_name = $("#l-name").val()
    phone_number = $("#contact").val()
    country = $("#country").val()
    state = $("#state").val()
    city = $("#city").val()
    zip_code = $("#zip").val()
    street_address = $("#address").val()
    customer_id = window.localStorage.getItem('customer_id')

    $.ajax({
        type: "post",
        url: "https://oneigsl.com/customer/update/v1/",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + window.localStorage.getItem('jwt_token')
        },
        data: JSON.stringify({
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "country": country,
            "state": state,
            "city": city,
            "zip_code": zip_code,
            "street_address": street_address
        }),
    
        success: function (data, text) {
            showToast('Personal Information Updated Successfully!')
            window.location.replace('profile-personal-information.php')
    
        },
        error: function (request, status, error) {
        console.log(error, status)
        if (request.status == 409) {
            showToast(request.responseJSON.detail)
        }
        else {
          showToast(request.responseText)
        }
        }
    });
    
}


function shippingAddressInfo(event) {

    event.preventDefault()
    from_name = $("#y-name").val()
    from_company = $("#company").val()
    from_email = $("#email").val()
    from_phone_no = $("#contact").val()
    from_country = $("#country").val()
    from_state = $("#state").val()
    from_city = $("#city").val()
    from_zip_code = $("#zip").val()
    from_street_address = $("#address").val()

    to_name = $("#r-name").val()
    to_company = $("#r-company").val()
    to_email = $("#r-email").val()
    to_phone_no = $("#r-contact").val()
    to_country = $("#r-country").val()
    to_state = $("#r-state").val()
    to_city = $("#r-city").val()
    to_zip_code = $("#r-zip").val()
    to_street_address = $("#r-address").val()

    let shipping_address_details = {

        "from_address":
           {
              "name": from_name,
              "company": from_company,
              "email": from_email,
              "phone_no": from_phone_no,
              "country": from_country,
              "state": from_state,
              "city": from_city,
              "zip_code": from_zip_code,
              "street_address": from_street_address,
           }
        ,
        "to_address":
            {
               "name": to_name,
               "company": to_company,
               "email": to_email,
               "phone_no": to_phone_no,
               "country": to_country,
               "state": to_state,
               "city": to_city,
               "zip_code": to_zip_code,
               "street_address": to_street_address,
            }
     }
        
    window.localStorage.setItem('shipping_address_details', JSON.stringify(shipping_address_details))
    var address_details = JSON.parse(window.localStorage.getItem('shipping_address_details'))
    // console.log(address_details)
        
}


function shippingDetails(event) {

    event.preventDefault()

    packaging_type = $("#packaging").val()
    no_of_packages = $("#no-of-packages").val()
    weight_per_package = $("#packaging-weight").val()
    departure_date = $("#shipping-date").val()

    console.log(packaging_type)
    console.log(no_of_packages)
    console.log(weight_per_package)
    console.log(departure_date)

    arrival_date = $("#shipping-date").val()
    base_rate = $("#base-rate").text();
    fuel_surcharge = $("#fuel-surcharge").text();
    res_del_surcharge = $("#res-del-surcharge").text();
    igs_pickup = $("#1igs-pickup").text();
    peak_surcharge = $("#peak-surcharge").text();
    est_total = $("#est-total").text();

    console.log(base_rate)
    console.log(fuel_surcharge)
    console.log(res_del_surcharge)
    console.log(igs_pickup)
    console.log(peak_surcharge)
    console.log(est_total)

}


function shippingHistory() {

    $.ajax({
        type: 'GET',
        url: 'https://oneigsl.com/shipment/v1/',
        headers: {
            "Authorization": "Bearer " + window.localStorage.getItem('jwt_token')
        },
        success: function (response) {

            console.log(response)

            for (var i=0; i<response["results"].length; i++) {

                if(response["results"][i]['status'].toLowerCase() == 'delivered') {
                    badge = 'success';
                }
                else if(response["results"][i]['status'].toLowerCase() == 'out_for_delivery') {
                    badge = 'info';
                }
                else if(response["results"][i]['status'].toLowerCase() == 'pending') {
                    badge = 'warning';
                }
                else if(response["results"][i]['status'].toLowerCase() == 'picked_up') {
                    badge = 'primary';
                }
                else {
                    badge = 'danger';
                }

                var  sr_no = i + 1
                var shipping_info = '<tr>\n' +
                    '                        <td>'+sr_no+'</td>\n' +
                    '                        <td>'+response["results"][i]['tracking_id']+'</td>\n' +
                    '                        <td>'+response["results"][i]['send_to']+'</td>\n' +
                    '                        <td>'+response["results"][i]['to_address']+'</td>\n' +
                    '                        <td>'+response["results"][i]['to_contact']+'</td>\n' +
                    '                        <td>'+response["results"][i]['booking_date']+'</td>\n' +
                    '                        <td>'+response["results"][i]['package_detail']+'</td>\n' +
                    '                        <td>'+response["results"][i]['package_weight']+'</td>\n' +
                    '                        <td>$354.17</td>\n' +
                    '                        <td>'+response["results"][i]['delivered_on']+'</td>\n' +
                    '                        <td>\n' +
                    '                            <div class="badge badge-'+badge+'">'+response["results"][i]['status']+'</div>\n' +
                    '                        </td>\n' +
                    '                        <td>\n' +
                    '                            <button class="btn-default-round btn-icon">\n' +
                    '                                <i class="fa fa-download"></i>\n' +
                    '                            </button>\n' +
                    '                        </td>\n' +
                    '                    </tr>'

                $("#shipping-history").append(shipping_info)
            }
            
        }
    });

}


function trackShipment() {

    
    // alert("tracking_id")
    window.location.replace('track.php')
    tracking_id = $("#tracking-id").val().toString()
    // alert(tracking_id)
    

    $.ajax({
        type: 'GET',
        url: 'https://oneigsl.com/shipment/v1/'+tracking_id+'/',
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + window.localStorage.getItem('jwt_token')
        },
        success: function (response) {
            
            document.getElementById('tracking-no').innerHTML = response['tracking_id'];
            document.getElementById('sender-name').innerHTML = response['sender'];
            document.getElementById('sender-location').innerHTML = response['from_address'];
            document.getElementById('recipient-name').innerHTML = response['send_to'];
            document.getElementById('recipient-location').innerHTML = response['to_address'];
            document.getElementById('booking-date').innerHTML = response['booking_date'];
            document.getElementById('status').innerHTML = response['status'];
            document.getElementById('delivery-date').innerHTML = response['delivered_on'];
            document.getElementById('delivery-time').innerHTML = "17:30";
            document.getElementById('signed-by').innerHTML = response['send_to'];
            
            document.getElementById("snackbar").style.display="none";
            document.getElementById("tracking-results").style.display="block";
            
        },

        error: function (request, status, error) {
            console.log(error, status)
            document.getElementById("tracking-results").style.display="none";
            document.getElementById("snackbar").style.display="block";
            if (request.status == 409) {
                showToast(request.responseJSON.detail)
            }
            if (request.status == 404) {
                showToast("No Results Found for this Tracking ID")
            }
            else {
              showToast(request.responseText)
            }
        }

    });

}


function changePassword(event) {

    event.preventDefault()
    old_password = $("#old-password").val()
    new_password = $("#new-password").val()
    confirm_password = $("#c-password").val()

    if (new_password != confirm_password) {
        showToast("Your new Passwords doesn't match!")
        return
    }

    $.ajax({
        type: "post",
        url: "https://oneigsl.com/customer/update/v1/",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + window.localStorage.getItem('jwt_token')
        },
        data: JSON.stringify({
            "old_password": old_password,
            "new_password": new_password
        }),
    
        success: function (data, text) {
            showToast('Password has been Updated Successfully!')
            // window.localStorage.setItem('jwt_token', '')
            window.location.replace('sign-in.php')
    
        },
        error: function (request, status, error) {
        console.log(error, status)
        if (request.status == 409) {
            showToast(request.responseJSON.detail)
        }
        else {
          showToast(request.responseText)
        }
        }
    });

}


function addSupportTicket(event) {

    event.preventDefault()
    full_name = $("#name").val()
    email = $("#email").val()
    phone_number = $("#contact").val()
    description = $("#message").val()

    $.ajax({
        type: "post",
        url: "https://oneigsl.com/customer/open-support-ticket/",
        headers: {
            "Content-Type": "application/json"
        },
        data: JSON.stringify({
            "name": full_name,
            "email_address": email,
            "contact_number": phone_number,
            "description": description
        }),
    
        success: function (data, text) {
            showToast('Your Ticket has been created Successfully!')
            // window.location.replace('profile-personal-information.php')
    
        },
        error: function (request, status, error) {
        console.log(error, status)
        if (request.status == 409) {
            showToast(request.responseJSON.detail)
        }
        else {
          showToast(request.responseText)
        }
        }
    });

}


function showToast(message) {

    // Add the "show" class to DIV
    console.log($('#snackbar').className)
    $('#snackbar').attr('class', 'snackbar show')
    $('#snackbar').text(message)

    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ $('#snackbar').attr( 'class', $('#snackbar').attr('class', 'snackbar show')); }, 4000);
}


