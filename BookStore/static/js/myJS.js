// JavaScript Document
$(document).ready(function(){//页面加载完成时
	var wH=$(window).height();//获取页面高度
	var _index=0;
	var Time=new Date();//获取页面时间
	setTimeout(function(){
		$(document).scrollTop(0);//刷新页面回到第一页
	},30);
	$(document).scrollTop(0);//刷新页面回到第一页
	$("#but ul li").click(function(){
		$(this).addClass("active").siblings().removeClass("active");
		_index=$(this).index();
		$("html,body").stop().animate({"scrollTop":_index*wH+"px"},900);
	});
	
	$(document).mousewheel(function(ev,dir){//鼠标滚轮事件  方位
		//alert(dir);
		//也可以不在function里写参数  用var d=arguments[1]
		if(new Date()-Time>900){
			Time=new Date();
			if(dir<0){
				_index++;
				_index%=7;
			}else if(dir>0){
				_index--;
				if(_index<0){_index=6;}
			}
			$("#but ul li").eq(_index).addClass("active").siblings().removeClass("active");
			$("html,body").stop().animate({"scrollTop":_index*wH+"px"},900);
		}
	});
});