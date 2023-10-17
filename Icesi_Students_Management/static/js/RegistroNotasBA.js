function agregarMateria() {
    contador++;
    const materiasDiv = document.getElementById("materias");

    const nuevaMateriaDiv = document.createElement("div");
    nuevaMateriaDiv.innerHTML = `
        <label for="codMateria${contador}" style="margin-top: 5%;">Codigo de la materia:</label>
        <br>
        <input type="text" id="codMateria${contador}" name="codMateria${contador}" required style="width: 70%;" class="campo-deshabilitable">
        <br>
        <label for="nombreMateria${contador}" style="margin-top: 5%;">Nombre de la materia:</label>
        <br>
        <input type="text" id="nombreMateria${contador}" name="nombreMateria${contador}" required style="width: 70%;" class="campo-deshabilitable">
        <br>
        <label for="creditosMateria${contador}" style="margin-top: 5%;">Creditos de la materia:</label>
        <br>
        <input type="number" id="creditosMateria${contador}" name="creditosMateria${contador}" required min="0" step="1" style="width: 10%;" class="campo-deshabilitable">
        <br>
        <label for="estatusMateria${contador}" style="margin-top: 5%;">Estatus de la materia:</label>
        <br>
        <select id="estatusMateria${contador}" name="estatusMateria${contador}" required style="width: 70%;" class="campo-deshabilitable">
            <option value="" disabled selected>Selecciona una opción</option>
            <option value="Materia Cancelada">Materia Cancelada</option>
            <option value="Materia en Curso">Materia en Curso</option>
            <option value="Materia completada">Materia completada</option>
        </select>
        <br>
        <label for="Nota${contador}" style="margin-top: 5%;">Nota final:</label>
        <br>
        <input type="number" id="Nota${contador}" name="Nota${contador}" required min="0.0" max="5.0" step="0.1" style="width: 10%;" class="campo-deshabilitable">
        <br>
    `;

    materiasDiv.appendChild(nuevaMateriaDiv);
}