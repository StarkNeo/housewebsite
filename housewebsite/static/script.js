
let setOption = (e) => {
    let sectionText = document.getElementById("input-search")
    let sectionOptions = document.getElementById("input-options")

    if (e === "option") {
        sectionOptions.style.display = "flex"
        document.getElementById('input-text').value=''
        document.getElementById('input-text').required=false
        document.getElementById('option').required=true
        sectionText.style.display = "none"
    }
    else{
        sectionOptions.style.display = "none"
        sectionText.style.display = "flex"
        document.getElementById('option').value=""
        document.getElementById('option').required=false
        document.getElementById('input-text').required=true
    }   

}




let btnReadAnswer = document.getElementById('read-answer');
let btnListenAnswer = document.getElementById('listen-answer')
let textareaAnswer =  document.getElementById('answer');
let audioAnswer = document.getElementById('audio-answer');
btnReadAnswer.addEventListener('click',()=>{
    if (textareaAnswer.style.display === 'flex') {
        textareaAnswer.style.display="none";    
    } else {
        textareaAnswer.style.display="flex";
    }
    
})
btnListenAnswer.addEventListener('click',()=>{
    if (audioAnswer.style.display === 'flex') {
        audioAnswer.style.display ='none';
    } else {
        audioAnswer.style.display ='flex';
    }
})

async function sendForm() {
    let textInput = document.getElementById('input-text').value;
    let optionInput = document.getElementById('option').value;
    let url = '/';
    let init = {
        method: 'POST',
        body: JSON.stringify({textInput, optionInput}),
        cache: 'default',
        headers: { 'Content-Type': 'application/json' }

    };

    try {
        let response = await fetch(url, init);
        let json = await response.json();
        alert(json.message)
        
    
    } catch (error) {
        console.log(error);
    }
    
    
}

