var branch,program,year,sem;
var Obj;
var k=[,,,,];
var key;
var count=0,count1=0,j=0,num=0;
function subj(){
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
    Obj = JSON.parse((this.responseText));
    }
};
//xmlhttp.open("GET", "data1.json", true);
//xmlhttp.send();
}
var d = (document.getElementById("data").innerHTML);
Obj = JSON.parse(d);
function store2(key){    
    branch=document.forms["info"]["branch"].value;
	if(key!=0){
	var id="program"+key;
	program=document.getElementById(id).value;
	
    var id="year"+key;   
	year=document.getElementById(id).value;

	var id="semester"+key;
	sem=document.getElementById(id).value;
	count++;
	add1(key);}
	else{
		count++;
		var element1=document.getElementById("subject1");
		var element2=document.getElementById("subject2");
		var element3=document.getElementById("subject3");
		var element4=document.getElementById("subject4");
		var element5=document.getElementById("subject5");
        element1.addEventListener("click",function(){
	    var p=1;
	     add1(p);
	});
        element2.addEventListener("click",function(){
	    var p=2;
	     add1(p);
	});
        element3.addEventListener("click",function(){
	    var p=3;
	     add1(p);
	});
        element4.addEventListener("click",function(){
	    var p=4;
	     add1(p);
	});
	element5.addEventListener("click",function(){
	    var p=5;
	     add1(p);
	});
	}
}
function store5(key){   
	var id="subject"+key;
	var p=document.getElementById(id).value;
	var i=0;
	do{
		if(p==k[i]){
			alert("choose another subject");
			k[(key-1)]="";
		    document.getElementById(id).value="";
			count1++;
			break;
			
		}
        i++;	
	}while(i<num);
	if(count1==0){
			k[(key-1)]=p;
		num++;
	}
	count1=0;
}

function add1(key){	
if(count>0){
var code="";
var id="subject"+key;
var selectobject=document.getElementById(id);
for(var r=selectobject.length-1;r>0;r--){
if(selectobject.options[r].value!=""){
selectobject.remove(r);}}

for(var i=0;i<(Obj.length);i++){
	if(branch==(Obj[i].fields.branch)){	
		if(program==(Obj[i].fields.program)){
			if(year==(Obj[i].fields.year)){
			    if(sem==(Obj[i].fields.semester)){
				var x1=document.getElementById(id);
					        var option=document.createElement("option");
							option.text=Obj[i].fields.name;
							option.id=key;
							option.value=Obj[i].fields.name;
							x1.add(option);
						           }
	            else
			continue;}
			else
				continue;
		}
		else
			continue;
		}
	else
		continue;
}
count=0;
}

}



