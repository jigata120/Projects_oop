// custom.js

//document.addEventListener('DOMContentLoaded', function() {     -------------    });


//document.querySelectorAll('button').forEach(function(button){     ---------    });
   //button.onclick = function(){     ---------    }
  //    document.querySelector('h1').style.color = button.dataset.color;

//document.querySelector('select').onchange = function() { ----------  });
                  //  document.querySelector('#hello').style.color = this.value; <h1  value="blue" ></h1>



document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#sub').disabled = true;
    document.querySelector('#task1').onkeyup = ()=>{
        if (document.querySelector('#task1').value.length >0 ) {
            document.querySelector('#sub').disabled = false;
        }   else{
            document.querySelector('#sub').disabled = true;

        }
    }

    document.querySelector('#form').onsubmit = () =>{
        const task =  document.querySelector('#task1').value;
        console.log(task.length);

        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#tasks2').appendChild(li);
        document.querySelector('#task1').value = '';
        return false;

    }
});