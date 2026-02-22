function appendValue(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function calculate() {
    let expression = document.getElementById("display").value;

    try {
        if (expression.trim() === "") {
            throw "Empty Input";
        }

        // Prevent invalid characters
        if (!/^[0-9+\-*/.() ]+$/.test(expression)) {
            throw "Invalid Characters";
        }

        let result = eval(expression);

        if (!isFinite(result)) {
            throw "Division by Zero";
        }

        document.getElementById("display").value = result;

    } catch (error) {
        document.getElementById("display").value = "Error";
    }
}