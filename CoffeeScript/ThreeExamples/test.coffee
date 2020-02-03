input_data ="hello how are you welcome to <b>Tutorials Point.</b>"
regex = /<b>(.*)<\/b>/
result = regex.exec(input_data)
console.log result