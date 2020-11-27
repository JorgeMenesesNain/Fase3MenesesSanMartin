$(function() 
      {
        $("#mi-formulario").validate({
             rules: {
                    email: {
                        required: true,
                        email: true
                    },
                    fono: "required",
                    fecha: "required",
                    nombre: "required",
                    apellido: "required" 
                }, //rules
            messages: {
                email: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                nombre: {
                    required: 'Ingresa un Nombre',
                    minlength: 'Caracteres insuficiente'
                },
                fono:{
                    required: 'Ingrese un número de celular',
                    minlength: 'Cantidad de digitos insuficiente'
                },
                fecha:{
                    required: 'Seleccione una fecha válida',
                    min: 'Fecha no corresponde'
                },
                apellido: {
                    required: 'Ingrese un Apellido',
                    minlength: 'Caracteres insuficiente'
                }
            }//messages
        }); //$('#mi-formulario').validate
    }); //function

    $(document).ready(function(){
        $("#btn1").click(function(){
            if($("#mi-formulario").valid()){
          alert("Pago realizado con exito!.");
            }
        });
      });    
    $(document).ready(function(){
        $("#prob").click(function(){
          $("#osito").animate({left: '100px'});
        });
      });

    $(document).ready(function(){
        $("#flip").click(function(){
          $(".panel").slideToggle("slow");
        });
      });

    $(document).ready(function(){
        $("#prob").click(function(){
          $("p").toggle();
        });
      });
