document.getElementById('send-btn').addEventListener('click',sendMessage);

async function sendMessage(){

    const userInput=document.getElementById('user-input').value;

    if(userInput==='') return;

    appendMessage(userInput,'user');

    document.getElementById('user-input').value='';

    try{

            const response=await fetch('http://127.0.0.1:8000/csa-api/v1/services/user_request',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                },

                body:JSON.stringify({

                    input_statement:userInput,
                    user_id:"xyz599"

                }),
            });

            if(!response.ok){
                const errorData=await response.json();
                if(errorData.detail=="intent not found or not supported"){

                    appendMessage("Sorry, I couldn`t understand your request, Please try Again in some time",'bot')

                    }
                    else{

                        throw new Error('Failed to Fetch response');

                    }
                    return;

            }

            const data=await response.json();
            console.log("API Response:",data)

            if(data.intent==="track_package"){

                if(data.service_response && data.service_response.length>0)
                {

                    appendTypingEffect(data.service_response);

                }
                else if(data.message){

                    appendMessage(data.message,'bot');

                }

           }
           else if(data.intent==="return_policy"){

                if(data.service_response && data.service_response.length>0){

                    appendTypingEffect(data.service_response);

                }
                else{

                    appendMessage("Sorry, I couldn{t process your request",'bot');

                }

           }

    }catch(error){

        console.error('Error:',error);
        appendMessage("Sorry, Something went wrong, Please try again",'bot');
    }


}

function appendMessage(message,sender){

    const chatBox=document.getElementById('chat-box');
    const messageDiv=document.createElement('div');
    messageDiv.classList.add('message');

    const messageContent=document.createElement('div');
    messageContent.classList.add(`${sender}-message`);
    messageContent.innerHTML=message;

    messageDiv.appendChild(messageContent);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop=chatBox.scrollHeight;

}

function appendTypingEffect(response){

    const chatBox=document.getElementById('chat-box');
    const typingDiv=document.createElement('div');
    typingDiv.classList.add('bot-message');
    typingDiv.id='typing-effect';
    chatBox.appendChild(typingDiv);

    const typed=new Typed('#typing-effect',{
        strings:[formatResponse(response)],
        typeSpeed:15,
        contentType:'html',
        onComplete:()=>{
        typingDiv.id=' ';

        },
    });
}

function formatResponse(response){

    let formattedResponse=`<p><strong>Thanks for contacting us, please find details below</strong></p>`;

    if(response[0].order_id){

        formattedResponse+=`
        <p><strong>Order ID:</strong>${response[0].order_id}</p>
        <p><strong>Current Status is:</strong>${response[0].delivery_status}</p>
        <p><strong>Expected Delivery Date:</strong>${response[0].expected_delivery_date}</p>
        `;
    }
    else if(response[0].type_of_policy){

        response.forEach(policy =>{
        formattedResponse+=`
        <p>Return policy for  ${policy.policy_product}:</p>
        <p>${policy.policy_details}</p>
        `;


        });

    }


return formattedResponse;

}