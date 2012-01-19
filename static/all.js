$(document).ready(function(){

  $('#task_name').autocomplete({
      source: '/pr/suggest/exercise/',
      // source: ["c++", "java", "php", "coldfusion", "coldfusion2", "coldfusion3", "javascript", "asp", "ruby", "жим"],    minLength: 2,
      select: function(event, ui) {
          $('#task_id').val( ui.item.id );
          $('#task_name').val( ui.item.label );
          console.log(ui.item);
      },
      focus: function( event, ui ) {
          $( "#task_name" ).val( ui.item.label );
          return false;
      }
  });

  $('#add').click(function(e){
      e.preventDefault();

      var a = $('#add_task').serializeArray();
      console.log(a);

      $('#add_task').submit();
  });


  $('.delete').click(function(e){
    if (confirm("точно удалять?")) {
      return true;
    }
    e.preventDefault();
    return false;
  });

  $('.sorted').sortable({
    items: 'tr.item',
    placeholder: "ui-state-highlight"
  });

  $('#save_order').click(function(e){
    e.preventDefault();
    show_loader();
    var res = $('.sorted').sortable('toArray');
    console.log(res);
    $.post('/pr/task/re_order/', {order:res.join('+')}, function(){ hide_loader(); }, 'json');
  });

  var show_loader = function(){
    globalLoader.show();
  };

  var hide_loader = function(){
    globalLoader.hide();
  };

  var update_ss_number = function(id, s_num){
      globalLoader.show();
      $.post('/pr/task/save_ss/', {number:s_num, task_id: id}, function(){ globalLoader.hide(); }, 'json');
  };

  $('.plus').click(function(e){
      e.preventDefault();
      var ss = $(this).parents('#toolbar').find('.super_set');
      var s_num = parseInt($(ss).html()) + 1;
      $(ss).html(s_num);
      var id = parseInt($(ss).parents('tr').attr('id').replace("task_id_", ""));
      update_ss_number(id, s_num);
  }).button({
    icons: {
      primary: "ui-icon-circle-arrow-e"
    },
    text: false
  });

  $('.minus').click(function(e){
      e.preventDefault();
      var ss = $(this).parents('#toolbar').find('.super_set');
      var s_num = parseInt($(ss).html()) - 1;
      if (s_num < 0) {
          s_num = 0;
      }
      $(ss).html(s_num);
      var id = parseInt($(ss).parents('tr').attr('id').replace("task_id_", ""));
      update_ss_number(id, s_num);
  }).button({
        icons: {
            primary: "ui-icon-circle-arrow-w"
        },
        text: false
    });
  
  
  


window.globalLoader = {
    ID:'globalLoader',
    entity:null,
    init:function(){
        if($('#'+globalLoader.ID).length){
            globalLoader.entity = $('#'+globalLoader.ID);
            return globalLoader;
        }
        $('<div id="'+globalLoader.ID+'"><div class="inner"></div></div>').appendTo($('body'));
        globalLoader.entity=$('#'+globalLoader.ID);
        globalLoader.setDefaultMessage();
        $( globalLoader.entity ).dialog({
            height: 70,
            modal: true,
            closeOnEscape: false,
             resizable: false,
             autoOpen: false
        });
        return globalLoader;
    },
    setDefaultMessage:function(){
        globalLoader.setMessage('Loading...');
        return globalLoader;
    },
    setMessage:function(message){
        $('.inner',globalLoader.entity).html(message);
        return globalLoader;
    },
    show:function(){
        $( globalLoader.entity ).dialog('open');
        return globalLoader;
    },
    hide:function(){
        $( globalLoader.entity ).dialog('close');
        globalLoader.setDefaultMessage();
        return globalLoader;
    }
};

  globalLoader.init();
  
}); // doc ready

