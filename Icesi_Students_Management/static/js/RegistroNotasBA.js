let contador = 1;

function agregarMateria() {
    contador++;
    const materiasDiv = document.getElementById("materias");

    const nuevaMateriaDiv = document.createElement("div");
    nuevaMateriaDiv.innerHTML = `
        <label for="codMateria${contador}" style="margin-top: 5%;">Codigo de la materia:</label>
        <br>
        <input type="text" id="codMateria${contador}" name="codMateria${contador}" required style="width: 70%;">
        <br>
        <label for="Nota${contador}" style="margin-top: 5%;">Nota:</label>
        <br>
        <input type="text" id="Nota${contador}" name="Nota${contador}" required  style="width: 10%;">
        <br>
    `;

    materiasDiv.appendChild(nuevaMateriaDiv);
}