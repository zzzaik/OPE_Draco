
function main() {


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

(function () {
   'use strict';

  	$('a.page-scroll').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top - 40
            }, 900);
            return false;
          }
        }
      });

	// affix the navbar after scroll below header
$('#nav').affix({
      offset: {
        top: $('header').height()
      }
});

	// skills chart
	$(document).ready(function(e) {
	//var windowBottom = $(window).height();
	var index=0;
	$(document).scroll(function(){
		var top = $('#skills').height()-$(window).scrollTop();
		console.log(top)
		if(top<-300){
			if(index==0){

				$('.chart').easyPieChart({
					easing: 'easeOutBounce',
					onStep: function(from, to, percent) {
						$(this.el).find('.percent').text(Math.round(percent));
					}
				});

				}
			index++;
		}
	})
	//console.log(nagativeValue)
	});


  	// Portfolio isotope filter
    $(window).load(function() {
        var $container = $('.portfolio-items');
        $container.isotope({
            filter: '*',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $('.cat a').click(function() {
            $('.cat .active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });

    });


    // CounterUp
	$(document).ready(function( $ ) {
		if($("span.count").length > 0){
			$('span.count').counterUp({
					delay: 10, // the delay time in ms
			time: 1500 // the speed time in ms
			});
		}
	});

  	// Pretty Photo
	$("a[rel^='prettyPhoto']").prettyPhoto({
		social_tools: false
	});

}());


}

function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
console.log(csrftoken);

//Ajax call
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function atualizarCatalogo () {
    let data = [];
    let images = $("[name=semClassificacao]");
    images.each(function (){
        imgId = images.find("input").val();
        estiloId = images.find("select").val();
        dict = {'imgId': imgId,'estiloId':estiloId};
        data.push(dict);
        console.log(dict);
    });


    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_catalogo/save_catalogo',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
            console.log(JSON.stringify(data));
        }
    });
}

function saveCatalogo () {
    let data = [];
    let images = $("[name=semClassificacao]");
    images.each(function (){
        imgId = images.find("input").val();
        estiloId = images.find("select").val();
        dict = {'imgId': imgId,'estiloId':estiloId};
        data.push(dict);
        console.log(dict);
    });

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_catalogo/save_catalogo',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
            console.log(JSON.stringify(data));
        }
    });
}

function savePortifolio () {
    let data = [];
    let images = $("[name=semClassificacao]");
    images.each(function (){
        imgId = images.find("input").val();
        estiloId = images.find("select").val();
        dict = {'imgId': imgId,'estiloId':estiloId};
        data.push(dict);
        console.log(dict);
    });

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_portifolio/save_portifolio',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
            console.log(JSON.stringify(data));
        }
    });
}

function atualizarCatalogo () {
    let data = {'action':'atualizar'}
    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/main/atualizar_catalogo',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
        }
    });
};

function atualizarPortifolio () {
    let data = {'action':'atualizar'}
    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/main/atualizar_portifolio',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
        }
    });
}

function filtrarEstilo () {
    let estilo = $('select[name=Estilo] option:selected').text();
    $('.gridFoto').each(function (){
        if($(this).attr('name') != "estilo_"+estilo){
            if($(this).css('display') != 'none'){
                $(this).hide();
            }
        } else {
            if($(this).css('display') == 'none'){
                $(this).show();
            }
        }
    });
}

function limparFiltro () {
    $('.gridFoto').each(function () {
        if($(this).css('display') == 'none'){
                $(this).show();
        }
    });
}

function novaPromocao () {
    let desc = $('input[name=desconto]').val();
    let data = {'desconto':desc/100}
    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_promos/nova_promocao',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
        }
    });
}

let listPromos = [];

function addImagemPromo(imgId) {
    listPromos.push({'imagemId':imgId});
}

function registrarPromocao () {
    let promoId = $('#containerHidden').attr('name');
    let validade = $('#inputValidade').val();
    let data = {'promoId':promoId, 'validade':validade, 'imagens':listPromos};

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_promos/registrar_promocao',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result);
            let seletor = $('div.seletorPromos');
                if (seletor.css('display') != 'none') {
                seletor.hide('fast');
                }
                listPromos = [];
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
            listPromos = [];
        }
    });

}

function contratarServico () {
    let imageId = $('#input_idImagem').val();
    let colorId = $('#select_cor option:selected');
    let sizeId = $('#select_tamanho option:selected');
    let localId = $('#select_regiao option:selected');
    let clientId = $('#select_cor').val();
    let promotion = false;

    let data = {'imageId':imageId, 'colorId':colorId, 'sizeId':sizeId, 'localId':localId, 'clientId':clientId , 'promotion':promotion};

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/user/registrar_servico',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result['Status']);
            let seletor = $('div.seletorServico');
                if (seletor.css('display') != 'none') {
                seletor.hide('fast');
                }
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
        }
    });

}


function showSelector (promoId) {
    let width = $('div.container').css('width');
    $('div.seletorPromos').css('width',width);
    $('#containerHidden').attr('name',promoId);
    let seletor = $('div.seletorPromos');
    if (seletor.css('display') == 'none') {
        seletor.show('slow');
    }
}

function showOrcamento (imageId,url,estiloComplex) {
    $('#input_idImagem').val(imageId);
    $('#largeFoto').attr('src',url);
    $('#input_complex').val(estiloComplex)
    let seletor = $('div.seletorServico');
    if (seletor.css('display') == 'none') {
        seletor.show('slow');
    };
}

function closeWindow (classe) {
    if($('div.'+classe).css('display') != 'none'){
        $('div.'+classe).hide('slow');
        $('#input_show_valor').text('')
    };
}

function calcularOrcamento () {
    let baseVal = parseInt($('#input_complex').val()) + parseInt($('#select_tamanho option:selected').attr('name'));
    let colorMult = parseInt($('#select_cor option:selected').attr('name'));
    let localMult = parseInt($('#select_regiao option:selected').attr('name'));
    let orcamento = (baseVal * 25) + colorMult + localMult;

    console.log(baseVal, colorMult, localMult);

    $('#input_show_valor').text('R$'+orcamento);


}

function getBool (e) {
    if (e=='on') {
        return 1
    } else {
        return 0
    }
}

function submitAnamnese () {

    let data = {
        	    'menor18Anos': getBool($('#souMenor').val()),
            	'rgResponsavel': $('#rgResponsavel').val(),
            	'cpfResponsavel': $('#cpfResponsavel').val(),
            	'dataNascResponsavel': $('#dataNascResponsavel').val(),
            	'nomeResponsavel': $('#nomeResponsavel').val(),
            	'enderecoResponsavel': $('#enderecoResponsavel').val(),
            	'cep': $('#cepRespon').val(),
            	'profissao': $('#profissaoRespon').val(),
            	'telefone': $('#telefoneRespon').val(),
            	'email': $('#emailRespon').val(),
        		'registroAcidentes': getBool($('#acidentesGraves').val()),
            	'dataAcidente': $('#dataAcidente').val(),
            	'localAcidente': $('#localAcidente').val(),
            	'comLesao': getBool($('#comLesao').val()),
            	'alergica': getBool($('#alergica').val()),
            	'descricaoAcidente': $('#descricaoAcidente').val(),
            	'nome': $('#nomeAnam').val(),
        		'genero': $('#generoAnam option:selected').val(),
            	'dataNasc': $('#dataNascAnam').val(),
            	'rg': $('#RGAnam').val(),
            	'cpf': $('#cpfAnam').val(),
            	'endereco': $('#endAnam').val(),
            	'foneResidencial': $('#foneAnam').val(),
            	'celular': $('#celAnam').val(),
            	'email': $('#emailAnam').val(),
            	'peso': $('#pesoAnam').val(),
            	'altura': $('#alturaAnam').val(),
            	'aspirina': getBool($('#aspirina').val()),
            	'herpes': getBool($('#Herpes').val()),
            	'hipertensao': getBool($('#Hipertensao').val()),
            	'hemofilia': getBool($('#Hemofilia').val()),
            	'tontura': getBool($('#Tonturas').val()),
            	'cancer': getBool($('#Cancer').val()),
            	'cardiopatia': getBool($('#Cardiopatia').val()),
            	'hiv': getBool($('#HIV').val()),
            	'menstruacao': getBool($('#Menstruada').val()),
            	'gravida': getBool($('#Gravida').val()),
            	'amamentando': getBool($('#Amamentando').val()),
            	'asma': getBool($('#Asma').val()),
            	'colesterol': getBool($('#Colesterol').val()),
            	'eplepsia': getBool($('#Epilepsia').val()),
            	'problemaRenal': getBool($('#ProblemaRenal').val()),
            	'diabetes': getBool($('#Diabetes').val()),
            	'marcaPasso': getBool($('#MarcaPasso').val()),
            	'lupus': getBool($('#Lupus').val()),
            	'circulatorio': getBool($('#Circulatorio').val()),
            	'glaucoma': getBool($('#Glaucoma').val()),
            	'respiratorio': getBool($('#Respiratorio').val()),
            	'psoriase': getBool($('#Psoriase').val()),
            	'hepatite': getBool($('#Hepatite').val()),
            	'coagulacao': getBool($('#Coagulacao').val()),
            	'depressao': getBool($('#Depressao').val()),
            	'gripeh1n1': getBool($('#GripeH1N1').val()),
            	'alergia': $('#alergiaAnam').val(),
            	'outrasTatuagens': $('#tatuagemAnam').val(),
            }

            console.log(data);

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/user/cadastraDados/cadastrar_cliente',
        method:'POST',
        contentType:'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result){
            alert(result['Status']);
            let seletor = $('div.seletorServico');
                if (seletor.css('display') != 'none') {
                seletor.hide('fast');
                }
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status +"-"+thrownError);
        }
    });

}














main();