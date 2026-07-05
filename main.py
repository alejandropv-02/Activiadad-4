import React, { useState } from 'react';

const Actividad4Form = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
  });

  const [errors, setErrors] = useState({
    nombre: '',
    email: '',
  });

  const validateField = (name, value) => {
    let errorMsg = '';

    if (name === 'nombre') {
      if (!value.trim()) {
        errorMsg = 'El nombre es obligatorio.';
      } else if (value.length < 3) {
        errorMsg = 'El nombre debe tener al menos 3 caracteres.';
      }
    }

    if (name === 'email') {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!value.trim()) {
        errorMsg = 'El correo electrónico es obligatorio.';
      } else if (!emailRegex.test(value)) {
        errorMsg = 'El formato de correo no es válido.';
      }
    }

    setErrors((prevErrors) => ({
      ...prevErrors,
      [name]: errorMsg,
    }));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));

    validateField(name, value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!errors.nombre && !errors.email && formData.nombre && formData.email) {
      alert('¡Formulario controlado y validado enviado con éxito!');
    } else {
      alert('Por favor, verifique los campos.');
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', fontFamily: 'Arial' }}>
      <h2>Actividad 4 - Formulario Controlado</h2>
      <form onSubmit={handleSubmit}>
        
        {/* Campo Nombre */}
        <div style={{ marginBottom: '15px' }}>
          <label>Nombre:</label>
          <input
            type="text"
            name="nombre"
            value={formData.nombre} // Enlace con el estado
            onChange={handleChange}  // Captura el cambio inmediato
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
          {errors.nombre && <p style={{ color: 'red', fontSize: '12px' }}>{errors.nombre}</p>}
        </div>

        {/* Campo Email */}
        <div style={{ marginBottom: '15px' }}>
          <label>Correo Electrónico:</label>
          <input
            type="email"
            name="email"
            value={formData.email}  // Enlace con el estado
            onChange={handleChange}  // Captura el cambio inmediato
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
          {errors.email && <p style={{ color: 'red', fontSize: '12px' }}>{errors.email}</p>}
        </div>

        <button type="submit" style={{ padding: '10px 15px', backgroundColor: '#007bff', color: 'white', border: 'none', cursor: 'pointer' }}>
          Enviar
        </button>
      </form>
    </div>
  );
};

export default Actividad4Form;