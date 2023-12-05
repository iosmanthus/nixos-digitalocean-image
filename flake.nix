{
  description = "NixOS image for DigitalOcean";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nixos-generators = {
      url = "github:nix-community/nixos-generators";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    { nixos-generators
    , ...
    }:
    let
      system = "x86_64-linux";
    in
    {
      packages.${system}.digitalocean-image = nixos-generators.nixosGenerate {
        inherit system;
        format = "do";
        modules = [ ./configuration.nix ];
      };
    };
}
