function updateFields(frm)
{
	//var doc = window.parent.frames['topFrame'].document;
	var doc = document;
	//var doc2 = window.parent.frames['mainFrame'].document;
	var elt;
	var eName;
	var indx;
	var val;
	var d1;
	var d2;
	var formElements = "";

	for (var n=0; n < frm.elements.length; n++)
	{
		elt = frm.elements[n];
		eName = elt.name;
		d1 = doc.getElementsByName(eName);
		//d2 = doc2.getElementsByName(eName);

		if ( d1.item(0) )
		{
			if ( elt.type == 'text' ) {
				//d1.item(0).value = d2.item(0).value;
				val = elt.value;
			}
			else if ( elt.type == 'textarea' ) {
				//d1.item(0).value = d2.item(0).value;
				val = elt.value;
			}

			else if ( elt.type == 'checkbox' ) {
				//d1.item(0).checked = d2.item(0).checked;
				val = elt.checked;
			}
			else if ( elt.type == 'select-one' ) {
				//d1.item(0).selectedIndex = d2.item(0).selectedIndex;
				val = elt.selectedIndex;
			}
			else if ( elt.type == 'hidden' ) {
				//d1.item(0).checked = d2.item(0).value;
				val = elt.value;
			}
			else if ( elt.type == 'radio' ) {
				indx = getSelectedID(d1);
				val = d1.length+"."+indx+"="+elt.checked;
				//d1[indx].checked = true;
			}
			//ADD THE ELEMENT
			if ( elt.type != 'button' ) {
				//formElements += n + " - " + eName + " : " + elt.type + " : " + val + "\n";
				formElements += "$msg.=$"+eName+ " = $_POST['"+eName+"'];\n";
			}
		}
	}
	alert("The elements in the form '" + frm.name + "' are:\n\n" + formElements);
}

function getSelectedID(group)
{
  for(var k=0;k<group.length;k++)
    if(group[k].checked) return k;
		else return "";
}


function setErrorLabel(elmtName, msg) {
	var n = document.getElementsByTagName('label').length;
	var lbl;
	for (var i=0; i<n; i++) {
		lbl = document.getElementsByTagName('label').item(i);
		if ( lbl.getAttribute('for') == elmtName)
			lbl.innerHTML = msg;
	}
	return msg;
}


function validateEmpty(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* This is a required field!\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validatecallBack(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* Oops! You forgot to indicate if you want a call back.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatemyPrayer(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* Oops! You didn't say who the prayer is for.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatePrayer(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* Oops! You didn't say who the prayer is for.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatemyInstrument(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* Oops! You forgot to indicate if you play any instrument.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatemyExperience(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "* Oops! You forgot to indicate if you have any prior Experience.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatemyOccupation(fld) {
    var error = "";

    if (fld.value.length == 0) {
        fld.style.background = 'Yellow';
        error = "*Huh! You forgot to indicate your Occupation/Position.\n"
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validateZip(fld) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter your zip code.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        fld.style.background = 'Yellow';
        error = "* The zip code is the wrong length.\n";
    } else if (illegalChars.test(fld.value)) {
        fld.style.background = 'Yellow';
        error = "* The zip code possibly contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatelastName(fld) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a name.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        fld.style.background = 'Yellow';
        error = "* The last name is the wrong length.\n";
    } else if (illegalChars.test(fld.value)) {
        fld.style.background = 'Yellow';
        error = "* The name contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validatefirstName(fld) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a name.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        fld.style.background = 'Yellow';
        error = "* The first name is the wrong length.\n";
    } else if (illegalChars.test(fld.value)) {
        fld.style.background = 'Yellow';
        error = "* The name contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validateName(fld) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a name.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        fld.style.background = 'Yellow';
        error = "* The name is the wrong length.\n";
    } else if (illegalChars.test(fld.value)) {
        fld.style.background = 'Yellow';
        error = "* The name contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validateCity(fld) {
    var error = "";
    var illegalChars = /[\w\s\-]/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a city name.\n";
    } else if (!illegalChars.test(trim(fld.value))) {
        fld.style.background = 'Yellow';
        error = "* The city name contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validateFaith(fld) {
    var error = "";
    var illegalChars = /[\w\s\-]/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "*OOps! You forgot to say if you were born again. It is a pre-requisite.\n";
    } else if (!illegalChars.test(trim(fld.value))) {
        fld.style.background = 'Yellow';
        error = "* TYour response contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validateAddress(fld) {
    var error = "";
    var illegalChars = /[\w\s\-]/; // allow letters, numbers, and underscores

    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter your home adddress.\n";
    } else if (!illegalChars.test(trim(fld.value))) {
        fld.style.background = 'Yellow';
        error = "* The home address contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validateEmail(fld) {
    var error="";
    var tfld = trim(fld.value);                        // value of field with whitespace trimmed off
    var emailFilter = /^[\w\.-]+@[\w\.-]+\.\w+$/i;
    var illegalChars= /[\(\)\<\>\,\;\:\\\"\[\]]/ ;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter an email address.\n";
    } else if (!emailFilter.test(tfld)) {              //test email for illegal characters
        fld.style.background = 'Yellow';
        error = "* Please enter a valid email address.\n";
    } else if (fld.value.match(illegalChars)) {
        fld.style.background = 'Yellow';
        error = "* The email address contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function validatePhone(fld) {
    var error="";
    var tfld = trim(fld.value);
    var phoneFilter = /^\d{3}?[\-]\d{3}?[\-]\d{4}|\d{3}?[\s]\d{3}?[\s]\d{4}|\d{10}$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a phone number.\n";
    } else if (!tfld.match(phoneFilter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid phone number.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatePhone1(fld) {
    var error="";
    var tfld = trim(fld.value);
    var phone1Filter = /^\d{3}?[\-]\d{3}?[\-]\d{4}|\d{3}?[\s]\d{3}?[\s]\d{4}|\d{10}$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter a phone number.\n";
    } else if (!tfld.match(phone1Filter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid phone number.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatePhone2(fld) {
    var error="";
    var tfld = trim(fld.value);
    var phone2Filter = /^\d{3}?[\-]\d{3}?[\-]\d{4}|\d{3}?[\s]\d{3}?[\s]\d{4}|\d{10}$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter your home phone number.\n";
    } else if (!tfld.match(phone2Filter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid home phone number.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validateDOB($dob){

list($ydob,$mdob,$ddob) = explode("-",$dob);
$year_diff = date("Y") - $ydob;
$month_diff = date("m") - $mdob;
$day_diff = date("d") - $ddob;

if ($day_diff < 0 || $month_diff < 0) {
$year_diff--;
return $year_diff;
} }

function validateDOB2($dob2){

list($ydob2,$mdob2,$ddob2) = explode("-",$dob2);
$year_diff = date("Y") - $ydob2;
$month_diff = date("m") - $mdob2;
$day_diff = date("d") - $ddob2;

if ($day_diff < 0 || $month_diff < 0) {
$year_diff--;
return $year_diff;
} }

function validZip(zip)
{
if (zip.match(/^[0-9]{5}$/)) {
return true;
}
zip=zip.toUpperCase();
if (zip.match(/^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$/)) {
return true;
}
if (zip.match(/^[A-Z][0-9][A-Z].[0-9][A-Z][0-9]$/)) {
return true;
}
alert('*** Bad ZIP.');
return false;
}

function validateNumber(fld) {
    var error="";
    var tfld = trim(fld.value);
    var numberFilter = /^[0-9]+$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter any number.\n";
    } else if (!tfld.match(numberFilter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid number.\n";
    } else if (tfld < 1) {
        fld.style.background = 'Yellow';
        error = "* Please enter a number greater than 0.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatepromoCode(fld) {
    var error="";
    var tfld = trim(fld.value);
    var promoCodeFilter = /^[0-9]+$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter your promo code.\n";
    } else if (!tfld.match(numberFilter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid promo code.\n";
    } else if (tfld < 1) {
        fld.style.background = 'Yellow';
        error = "* Please enter a code greater than 0.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}

function validatebookingNumber(fld) {
    var error="";
    var tfld = trim(fld.value);
    var bookingNumberFilter = /^[0-9]+$/;
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "* You didn't enter any number.\n";
    } else if (!tfld.match(bookingNumberFilter)) {
        fld.style.background = 'Yellow';
        error = "* Please enter a valid number.\n";
    } else if (tfld < 1) {
        fld.style.background = 'Yellow';
        error = "* Please enter a number greater than 0.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


function trim(s)
{
  return s.replace(/^\s+|\s+$/, '');
}
