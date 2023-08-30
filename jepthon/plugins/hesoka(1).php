<?php 
/*
BY = @HESOKA_59
الملف للونسة فط لا اكثر
*/
ob_start();
$API_KEY = " النوكن"; 

define('API_KEY',$API_KEY);
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$chat_id = $message->chat->id;
$text = $message->text; 
$admin = 561006376; // ايديك ;
$abowatan = "TM_Saeed"; // معرف قناتك بدون @
$albot = "hesoka_88robot"; // معرف البوت بدون @
$data = $update->callback_query->data;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 = $update->callback_query->message->message_id;
$name = $update->message->from->first_name;
$sudo = 561006376;
$u = explode("\n",file_get_contents("data/memb.txt"));
$c = count($u)-1;
if ($update && !in_array($chat_id, $u)) {
    file_put_contents("data/memb.txt", $chat_id."\n",FILE_APPEND);
  }
$about = file_get_contents("data/about.txt");

$u = explode("\n",file_get_contents("memb.txt"));
$m = count($u)-1;
$modxe = file_get_contents("usr.txt");
if ($update && !in_array($chat_id, $u)) {
file_put_contents("memb.txt", $chat_id."\n",FILE_APPEND);
}
if ($text == 'المشتركين') {
$m = count($u)-1;
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=> " عدد مشتركين البوت :- { $m }" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if (preg_match("/\/bc .*/", $text) and $chat_id == 493160132) {
$f = explode("\n", file_get_contents("memb.txt"));
$text = str_replace("/bc ", "", $text);
for ($i=0; $i < count($f); $i++) { 
bot("sendMessage",[
"chat_id"=>$f[$i],
"text"=>$text
]);
}
}
if($text == "/start"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"🍷 اهلا بكم ازائي الكرام في بوت ابو تحسين 🍷

🥃 البوت مصنوع للونسة فقط لا اكثر🥃

🍹اي ستسار تعال خاص @HESOKA_59  🍹

🍓 ارس كلمة  ( ابو تحسين ) لتشغيل البوت 🍓",
 ]);
 }
if($text == 'ابو تحسين'){
bot('sendMessage',[ 
'chat_id'=>$chat_id, 
'text'=>'هلا خوية تفضل', 
'reply_markup'=>json_encode([ 
'keyboard'=>[ 
[ 
['text'=>'اريد لفة'] 
]
]
]) 
]);
}

if($text == 'اريد لفة'){
bot('sendMessage',[ 
'chat_id'=>$chat_id, 
'text'=>'خوية عدنة 3 انواع لفات ختار لفة', 
'reply_markup'=>json_encode([ 
'keyboard'=>[ 
[ 
['text'=>'لفة فلافل🍔'] 
,['text'=>'لفة سبموسه🌮'] 
,['text'=>'لفة كص 🥓'] 
]
]
]) 
]);
}

if($text == "لفة فلافل🍔"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"خوية لفة الفلافل سعرهة 500 دينار💵
ارسل رقم 500 لشراء اللفة 💵",
 ]);
 }
 
 if($text == "لفة سبموسه🌮"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"خوية لفة السمبوسه سعرهة 1000 دينار💵
ارسل رقم 1000 لشراء اللفة 💵",
 ]);
 }
 
  if($text == "لفة كص 🥓"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"خوية لفة الكص سعرهة 2000 دينار💵
ارسل رقم 2000 لشراء اللفة 💵",
 ]);
 }
 
 if($text == "500"){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>"https://scontent.fbsr5-1.fna.fbcdn.net/v/t1.0-9/32815564_136869117172190_9091707739926691840_n.jpg?_nc_cat=0&oh=321b1b28b1f7bc27a61c69d2d431d61c&oe=5B8B9572",
 ]);
 }
 
  if($text == "1000"){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>"https://scontent.fbsr5-1.fna.fbcdn.net/v/t1.0-9/32769735_136871590505276_4671469463516741632_n.jpg?_nc_cat=0&oh=c14bd1454228caef47e09366d33354c6&oe=5B83F528",
 ]);
 }
 
  if($text == "2000"){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>"https://scontent.fbsr5-1.fna.fbcdn.net/v/t1.0-9/32929386_136873087171793_981126351819898880_n.jpg?_nc_cat=0&oh=78948a80a7cf211d80c05b2fc1e54162&oe=5B868019",
 ]);
 }
 if($text == "500"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"😘 بلعافية حبيبي 😘",
 ]);
 }
 
  if($text == "1000"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"😘 بلعافية حبيبي 😘",
 ]);
 }
 
  if($text == "2000"){
 bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"😘 بلعافية حبيبي 😘",
 ]);
 }
?>