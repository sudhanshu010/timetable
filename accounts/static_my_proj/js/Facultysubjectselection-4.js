var branch,program,year,sem;
var Obj;
var k=[,,,,];
var key;
var count=0,count1=0,j=0,num=0;
function subj(){
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
    Obj = JSON.parse("{{data}}");
    document.write(typeof(Obj))
    }
};
//xmlhttp.open("GET", "data.json", true);
//xmlhttp.send();
}
var d = (document.getElementById("data").innerHTML);
document.write('heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
document.
 Obj = JSON.parse(d);
 document.write(typeof(Obj))
 document.write(Obj[0].fields.name)

function store1(){
	branch=document.forms["info"]["branch"].value;
	count++;
}
function store2(key){
    var id="program"+key;
	program=document.getElementById(id).value;

    var id="year"+key;
	year=document.getElementById(id).value;

	var id="semester"+key;
	sem=document.getElementById(id).value;
	count++;
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
for(var i=0;i<Obj.length;i++){
	if(branch==(Obj[i].department)){
		if(program==(Obj[i].program)){
			if(sem==(Obj[i].semester)){
				var x1=document.getElementById(id);
				for(j=0;j<(Obj[i].subjects.length());j++){
					        var option=document.createElement("option");
							option.text=Obj[i].subjects[j];
							option.id=key;
							option.value=Obj[i].subjects[j];
							x1.add(option);
					}
				break;
	           }
	        else
				continue;}
		else
			continue;
		}
	else
		continue;
}
count=0;
}
}

