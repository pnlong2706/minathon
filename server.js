const http = require("http");
const fs = require("fs");
const URL = require("url");

var users, info;
fs.readFile('users.JSON', (err, data) => {
    if (err) throw err;
    users = JSON.parse(data);
});

fs.readFile('infomation.JSON', (err, data) => {
    if (err) throw err;
    info = JSON.parse(data);
});

function hash(s) {
    let N = s.length;
    let cs = "";
    for(let i = 0; i<N; i++) {
      cs += String.fromCharCode((s[i].charCodeAt(0) * 10007 + 1063 )%26 + 97);675
      cs += s[i%2];
    }
    return cs;
}

const server = http.createServer((req, res) => {
    
    let url_ = URL.parse(req.url, true)
    console.log(req.url);
    if( req.url === "/" ) {
        res.writeHead(200, { "Content-Type": "text/html" });
        fs.readFile("index.html", (err, data) => {
            if (err) throw err;
            res.end(data);
        });
    }

    else if( req.url === "/checkvalid" && req.method == "POST" ) {
        let body = ""
        req.on("data", function (chunk) {
            body += chunk ;
            console.log(body);
        });
        req.on("end", function () {
            let id = body.split("=")[0]
            let pass = body.split("=")[1]
            
            if(users.hasOwnProperty(id)) {
                //console.log(users[id]);
                if( users[id] == pass ) res.end(hash(pass));
                else res.end("-1");
            }
            else res.end("-1"); 
        });
    }

    else if( url_.pathname === "/user_info" ) {
        //console.log(users[id]);
        //console.log(hp_check);
        let id = url_.search.substring(4);
        let inf = info[id];
        fs.readFile("user_info.html", (err, data) => {
            if (err) throw err;
            data = data + "<script> user_name = '" + inf["name"] +  "';  user_mail = '"+ inf["email"] +"'; user_dob = '"+ inf["birthday"] +"'; user_char = '"+ inf["characteristic"] +"'; user_hobb = '"+ inf["hobbies"] +"'; user_addinf = '"+ inf["addInf"] +"';" ;
            data = data +  "document.getElementById('name').value = user_name; document.getElementById('email').value = user_mail; document.getElementById('dob').value = user_dob;";
            data = data +  "document.getElementById('characteristics').value = user_char; document.getElementById('hobbies').value = user_hobb; document.getElementById('additional_info').value = user_addinf;";
            data = data +  "current_user_id = '"+ id +"'; current_hp = '"+ hash(users[id]) +"';  </script>";
            res.end(data);
        });
    }

    else if( url_.pathname === "/user" ) {
        //console.log(users[id]);
        //console.log(hp_check);

        id = url_.search.split("?")[1].split("=")[1];
        hp = url_.search.split("?")[2].split("=")[1];

        console.log(id);
        console.log(hp);

        if(users.hasOwnProperty(id) && hash(users[id]) == hp) {
            console.log("XX");
            fs.readFile("index.html", (err, data) => {
                if (err) throw err;
                res.end( data + "<script> current_user_id = '"+id+"'; document.getElementById('login_button').innerHTML = current_user_id; document.getElementById('log_out').style.display = 'inline-block'; document.getElementById('login_button').onclick = function() { location.assign('http://192.168.211.250:3000/user_info?id=' + current_user_id); }; </script>" );
            });
        }
        else {
            fs.readFile("index.html", (err, data) => {
                if (err) throw err;
                res.end(data);
            });
        }
    }   

    else if( url_.pathname === "/chatbox" ) {
        let id = url_.search.split("=")[1];
        fs.readFile("chat_box.html", (err, data) => {
            if (err) throw err;
            res.end(data+ "<script> current_user_id = '"+ id +"'; current_hp = '"+ hash(users[id]) +"';  </script>" );
        });
    }

    else if( url_.pathname === "/filter" ) {
        let id = url_.search.split("=")[1];
        fs.readFile("filter.html", (err, data) => {
            if (err) throw err;
            res.end(data + "<script> current_user_id = '"+ id +"'; current_hp = '"+ hash(users[id]) +"';  </script>" );
        });
    }

    else if( url_.pathname === "/mentor" ) {
        let id = url_.search.split("=")[1];
        fs.readFile("mentor.html", (err, data) => {
            if (err) throw err;
            res.end(data + "<script> current_user_id = '"+ id +"'; current_hp = '"+ hash(users[id]) +"';  </script>" );
        });
    }

});

server.listen(3000, () => {
    console.log('Server listening on port 3000');
});
