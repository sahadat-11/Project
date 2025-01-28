document.getElementById('update-form').addEventListener('submit',(event)=>{
    event.preventDefault()
    const form=event.target
    const update_form=new FormData(form)
    fetch_api(update_form)
})

const fetch_api=async payload=>{
    const res=await fetch(`http://127.0.0.1:5000/update-user/${localStorage.getItem('id')}`,{
        method:"PUT",
        body:payload
    })
    const data=await res.json()
    console.log(data)
}