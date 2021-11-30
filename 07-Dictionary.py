monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions)
print(monthConversions["Dec"])
print(monthConversions.get("Aug"))
# Cuando se le pasa un valor que no existe en el dictionary, devuelve por default none
print(monthConversions.get("Termidor"))
# Tambien puedo especificar el valor por default al no encontrar un key valido
print(monthConversions.get("Termidor", "Se usa el calendario gregoriano"))
