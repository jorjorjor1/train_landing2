
    /* этот код помечает картинки, для удобства разработки */
    let i = 1;
    for(let li of carousel.querySelectorAll('li')) {
      li.style.position = 'relative';
      // li.insertAdjacentHTML('beforeend', `<span style="position:absolute;left:0;top:0">${i}</span>`);
      i++;
    }

    /* конфигурация */
    let width = 300; // ширина картинки
    let count = 3; // видимое количество изображений

    let list = carousel.querySelector('ul');
    let listElems = carousel.querySelectorAll('li');

    let position = 0; // положение ленты прокрутки

    carousel.querySelector('.prev').onclick = function() {
      // сдвиг влево
      position += width * count;
      // последнее передвижение влево может быть не на 3, а на 2 или 1 элемент
      position = Math.min(position, 0)
      list.style.marginLeft = position + 'px';
    };

    carousel.querySelector('.next').onclick = function() {
      // сдвиг вправо
      position -= width * count;
      // последнее передвижение вправо может быть не на 3, а на 2 или 1 элемент
      position = Math.max(position, -width * (listElems.length - count));
      list.style.marginLeft = position + 'px';
    };


$(document).ready(function () {
  $("a").click(function () {
      var elementClick = $(this).attr("href");
      var destination = $(elementClick).offset().top - 120;
      if ($.support.Safari) {
          $('body').animate({ scrollTop: destination }, 1100); //1100 - скорость
      } else {
          $('html').animate({ scrollTop: destination }, 1100);
      }
      return false; 
  });
});


$(window).on('load', function(){
  var top = $(window.location.hash).offset().top-120;
  $('html,body').stop().animate({
    scrollTop: top
  }, 1000);
});

$(document).ready(function () {
  $("a").click(function () {
    var elementClick = $(this).attr("href");
    var destination = $(elementClick).offset().top - 120;
  $('html').scrollTo(destination)
  })
});


$(document).ready(function(){
  $('.owl-one').owlCarousel({
      loop:true,
      margin:10,
      nav:true,
      touchDrag  : true,
      mouseDrag  : false,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:2
          },
          1000:{
              items:3
          }
      }
  });

  $('.owl-two').owlCarousel({
      loop:true,
      margin:10,
      nav:true,
      touchDrag  : true,
      mouseDrag  : false,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:2
          },
          1000:{
              items:3
          }
      }
  });

});






// Get the modal
var images = document.querySelectorAll(".image-for-modal");
var modal = document.getElementById("myModal-image");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption-image");
for(let i = 0; i < images.length; i++){
  images[i].onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }
}


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-image")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}

$(document).on('submit', '#post-form', function(e){
  // e.preventDefault();

  $.ajax({
      type:'POST',
      url:'/page/',
      data:{
          'email_contact':$("#email_contact").val(),
          'tel_contact':$('#tel_contact').val(),
          'question':$('#question').val(),
          'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
      },
      success: searchSuccess2,
      dataType: 'html',
      statusCode: {
          500: function() {
              raiseError();}
          },

      
  })
  return false;
});

function searchSuccess2 (data, textStatus, jqXHR){
  $('#class-for-notice').html(data)
}
function raiseError(){
  var errorNotice = document.createElement("div")
  errorNotice.className = 'alert alert-danger';
  errorNotice.role = 'alert'
  errorNotice.innerHTML = 'Заявка не отправлена, проверьте введенные данные'
  document.getElementById('class-for-notice').appendChild(errorNotice);
}