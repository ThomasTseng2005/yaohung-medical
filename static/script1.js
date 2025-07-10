// Transparent

var buttonPressed = 0;
var delayInMilliseconds = Math.max(window.innerWidth) / 7;
const disableBodyScroll = bodyScrollLock.disableBodyScroll;
const enableBodyScroll = bodyScrollLock.enableBodyScroll;
const targetElementOne = document.querySelector('#targetelementone');
const targetElementTwo = document.querySelector('#targetelementtwo');
var ua = navigator.userAgent.toLowerCase();
var userAgent = window.navigator.userAgent;
var check = false;
var isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);

function burgerClick() {
  $('.hamburger').toggleClass('is-active');
  if (buttonPressed === 0) {
    disableScroll();
    document.getElementById('hidden-links').style.transform = 'translateX(0%)';
    document.getElementById('hid-link-two').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.3s';
    document.getElementById('hid-link-three').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.4s';
    document.getElementById('hid-link-four').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.5s';
    document.getElementById('hid-link-five').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.6s';
    document.getElementById('hid-link-six').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.7s';
    document.getElementById('hid-link-seven').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.8s';
    document.getElementById('hid-link-eight').style.animation =
      'hiddenLinkFadeIn 0.5s ease forwards 0.9s';
    document.getElementById('nav-link-one').style.display = 'none';
    document.getElementById('nav-link-two').style.display = 'none';
    document.getElementById('nav-link-three').style.display = 'none';
    document.getElementById('nav-link-four').style.display = 'none';
    setTimeout(function () {
      try {
        document.getElementById('mainNavbar').style.background = 'transparent';
        document.getElementById('path1').style.fill = 'white';
        document.getElementById('path2').style.fill = 'white';
        document.getElementById('path3').style.fill = 'white';
        document.getElementById('path4').style.fill = 'white';
        document.getElementById('path5').style.fill = 'white';
      } catch (err) {
        console.log(err);
      }
    }, delayInMilliseconds);
    buttonPressed = 1;
  } else {
    enableScroll();
    document.getElementById('hidden-links').style.transform =
      'translateX(100%)';
    document.getElementById('hid-link-two').style.animation = '';
    document.getElementById('hid-link-three').style.animation = '';
    document.getElementById('hid-link-four').style.animation = '';
    document.getElementById('hid-link-five').style.animation = '';
    document.getElementById('hid-link-six').style.animation = '';
    document.getElementById('hid-link-seven').style.animation = '';
    document.getElementById('hid-link-eight').style.animation = '';
    setTimeout(function () {
      try {
        document.getElementById('mainNavbar').style.background = '';
        $('nav').toggleClass('scrolled', $(window).scrollTop() > 50);
        document.getElementById('path1').style.fill = '';
        document.getElementById('path2').style.fill = '';
        document.getElementById('path3').style.fill = '';
        document.getElementById('path4').style.fill = '';
        document.getElementById('path5').style.fill = '';
        $('.brand-path').toggleClass(
          'scrolled-brand',
          $(this).scrollTop() > 50
        );
        document.getElementById('nav-link-one').style.display = 'inline';
        document.getElementById('nav-link-two').style.display = 'inline';
        document.getElementById('nav-link-three').style.display = 'inline';
        document.getElementById('nav-link-four').style.display = 'inline';
      } catch (err) {
        console.log(err);
      }
    }, delayInMilliseconds);
    buttonPressed = 0;
  }
}

$(window).scroll(function () {
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
  $('.brand-path').toggleClass('scrolled-brand', $(this).scrollTop() > 50);
  $('.nav-links-hide').toggleClass(
    'scrolled-links',
    $(window).scrollTop() > 50
  );
  $('.hamburger-inner').toggleClass(
    'scrolled-burger-inner',
    $(window).scrollTop() > 50
  );
});

function disableScroll() {
  (function (a) {
    if (
      /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(
        a
      ) ||
      /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
        a.substr(0, 4)
      )
    )
      check = true;
  })(navigator.userAgent || navigator.vendor || window.opera);
  if (check === true) {
    if (isSafari) {
      document.body.style.position = 'fixed';

      scrollallow = false;
    } else {
      document.body.style.overflowY = 'hidden';
    }
  } else {
    disableBodyScroll(targetElementOne);
    disableBodyScroll(targetElementTwo);
  }
}

function enableScroll() {
  (function (a) {
    if (
      /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(
        a
      ) ||
      /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
        a.substr(0, 4)
      )
    )
      check = true;
  })(navigator.userAgent || navigator.vendor || window.opera);
  if (check === true) {
    if (isSafari) {
      document.body.style.position = 'relative';
      $('nav').removeClass('scrolled', $(this).scrollTop() > 50);
      $('.brand-anchor').removeClass(
        'brand-scrolled',
        $(window).scrollTop() > 50
      );
      $('.logo').removeClass('logo-scrolled', $(window).scrollTop() > 50);
      $('.nav-links').removeClass('links-scrolled', $(window).scrollTop() > 50);
      $('.nav-links li').removeClass('li-scrolled', $(window).scrollTop() > 50);
      $('.burger-link').removeClass(
        'burger-scrolled',
        $(window).scrollTop() > 50
      );
      $('.burger div').removeClass(
        'burger-link-scrolled',
        $(window).scrollTop() > 50
      );
      scrollallow = true;
    } else {
      document.body.style.overflowY = 'visible';
    }
  } else {
    enableBodyScroll(targetElementOne);
    enableBodyScroll(targetElementTwo);
  }
}

function appointmentClick(event) {
  event.preventDefault(); // 防止預設的連結行為
  const userAgent = window.navigator.userAgent;
  const text =
    '若有就醫、檢查等需求請來電02-29840101洽詢，受理時間為開診時間：週一至週五 9:00～12:30，14:00～16:30，17:30～20:30\n \n ＊初診僅受理現場掛號，請及早來診，歡迎來電洽詢。\n ＊當診滿額即會截止掛號，時間浮動，請盡早到診或來電掛號/報到。\n \n 電話：02-2984-0101\n \n 地址：新北市三重區重新路三段107號1樓';

  // 行動裝置
  if (/Mobi|Android/i.test(userAgent)) {
    if (confirm(text) == true) {
      window.location.href = event.currentTarget.href;
    } else {
      return;
    }
  } else {
    // 電腦版
    alert(text);
  }
}
$(document).ready(function () {
  fetch('/static/news/config.json')
    .then((response) => response.json())
    .then((data) => {
      const now = new Date();
      // console.log('now', now);
      const notifications = data.notifications || [];
      // console.log('notifications', notifications);

      // 檢查是否有任何一組區間符合現在時間
      const isInNotificationPeriod = notifications.some((period) => {
        const start = new Date(period.startDate);
        const end = new Date(period.endDate);
        // console.log('start', start);
        // console.log('end', end);
        return now >= start && now <= end;
      });
      // console.log('isInNotificationPeriod', isInNotificationPeriod);

      if (isInNotificationPeriod) {
        $('#newsModal').modal('show');
        $('#newsModal').on('hidden.bs.modal', function () {
          $('#newsModal1').modal('show');
          // console.log($('#newsModal1Video'));
        });
      } else {
        $('#newsModal1').modal('show');
      }
    })
    .catch((error) => {
      console.log('無法讀取config.json:', error);
    });

  $('#newsModal1').on('hidden.bs.modal', function () {
    // $('#newsModal1Video').remove(); // 移除 iframe
    $('#newsModal2').modal('show');
  });
});
