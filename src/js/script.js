function greet() {
    var name = document.getElementById('input').value;
    var outputDiv = document.getElementById('output');
    outputDiv.textContent = 'Hello, ' + name + '!';
}