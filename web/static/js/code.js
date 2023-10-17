$(function(){
  $.get('/graph', function(result) {
    var cy =window.cy = cytoscape({
		container: document.getElementById('cy'),	  // 定义需要渲染的容器
		style:cytoscape.stylesheet()
		.selector('node[labels = "STANDARD"]').css({'background-color': '#F5A45D','content': 'data(name)','font-size': '10px','font-family': '微软雅黑'}) //节点样式
		.css({
		'width': 30, // 设置节点宽度（以像素为单位）
		'height': 30 // 设置节点高度（以像素为单位）
			})
		.selector('node[labels = "FENBU" | labels = "ZIFENBU"]').css({'background-color': '#6FB1FC','content': 'data(name)','font-size': '10px','font-family': '微软雅黑'})
		.css({
		'width': 20, // 设置节点宽度（以像素为单位）
		'height': 20 // 设置节点高度（以像素为单位）
			})
		.selector('edge').css({'curve-style': 'bezier','target-arrow-shape': 'triangle','line-color': '#ffaaaa','target-arrow-color': '#ffaaaa','content': 'data(relationship)','font-size': '6px','font-family': '微软雅黑'}) //边线样式
		.selector(':selected').css({'background-color': 'black','line-color': 'black','target-arrow-color': 'black','source-arrow-color': 'black','opacity': 1}) //点击后节点与边的样式
		.selector('.faded').css({'opacity': 0.25,'text-opacity': 0}),
        layout: {
			name: 'cose',
			animate: true, // 是否启用布局动画，可选
			nodeRepulsion: 80000, // 节点之间的排斥力，可选
			componentSpacing: 40, // 组件之间的间距，可选
			//idealEdgeLength: 100000, // 边的理想长度，可选
        	}, 
      elements: result.elements
	});
	cy.elements().qtip({ //点击elements处的提醒
		content: //function(){ return 'Example qTip on ele ' + this.id() },
			{text:function(){ return "规范编号：" + this.data('S_ID')  +  "\n生效时间：" + this.data('start_time')  + "\n下载链接：" + this.data('url')},
			title:function(){ return this.data('name') }},
		position: {
			my: 'top center',
			at: 'bottom center'
		},
		style: {
			classes: 'qtip-bootstrap',
			tip: {
				width: 16,
				height: 8
			}
		}
	});

			// call on core,点击空白处的提醒
//	cy.qtip({
//		content: 'Example qTip on core bg',
//		position: {
//			my: 'top center',
//			at: 'bottom center'
//		},
//		show: {
//			cyBgOnly: true
//		},
//		style: {
//			classes: 'qtip-bootstrap',
//			tip: {
//				width: 16,
//				height: 8
//			}
//		}
//	});
}, 'json');
});